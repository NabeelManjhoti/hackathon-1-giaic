from typing import List, Optional
from ..models.query import QueryModel, QueryMode
from ..models.response import ResponseModel, Reference
from ..models.user_selection import UserSelectionModel
from ..core.vector_store import VectorStore
from ..services.embedding_service import EmbeddingService
from ..services.reference_service import ReferenceService
from ..services.chat_service import ChatService
from ..core.chat_config import ChatConfig
from ..core.logging import log_request, log_response, log_error


class RAGService:
    """
    Main service for handling RAG queries with both full-book and selected-text modes.
    """

    def __init__(self, vector_store: VectorStore, embedding_service: EmbeddingService):
        self.vector_store = vector_store
        self.embedding_service = embedding_service
        self.reference_service = ReferenceService(vector_store)
        self.chat_service = ChatService(ChatConfig.get_default_config())

    async def process_query(self, query_model: QueryModel) -> ResponseModel:
        """
        Process a query based on the specified mode (full-book or selected-text).

        Args:
            query_model: The query model containing the question and mode

        Returns:
            ResponseModel with the answer and references
        """
        try:
            # Log the incoming request
            log_request("anonymous", query_model.text, query_model.mode.value)

            # Generate embedding for the query
            query_embedding = await self.embedding_service.create_embedding(query_model.text)

            # Retrieve relevant content based on mode
            if query_model.mode == QueryMode.FULL_BOOK:
                relevant_chunks = self.vector_store.search(query_embedding, top_k=5)
            else:  # SELECTED_TEXT mode
                # In selected text mode, we directly use the selected text as context
                # This follows the direct injection approach mentioned in research.md
                if query_model.selected_text:
                    # For selected text mode, we create a context from the selected text
                    # and related content rather than doing a general search
                    selected_text_embedding = await self.embedding_service.create_embedding(
                        query_model.selected_text
                    )
                    relevant_chunks = self.vector_store.search(selected_text_embedding, top_k=5)

                    # Filter results to ensure they're related to the selected text
                    # In a real implementation, we might use reranking here as mentioned in research.md
                else:
                    relevant_chunks = self.vector_store.search(query_embedding, top_k=5)

            # Generate response using the retrieved chunks
            response_content = await self._generate_response(
                query_model.text,
                relevant_chunks
            )

            # Create references from the retrieved chunks using the reference service
            references = self.reference_service.create_references_from_chunks(relevant_chunks)

            # Calculate confidence score based on various factors
            confidence_score = self._calculate_confidence_score(
                relevant_chunks,
                query_model.text,
                response_content
            )

            # Create response model
            response = ResponseModel(
                query_id=query_model.id,
                content=response_content,
                references=references,
                confidence_score=confidence_score
            )

            # Log the response
            log_response("anonymous", query_model.id, response_content, response.confidence_score or 0.0)

            return response

        except Exception as e:
            log_error(e, f"Processing query {query_model.id}")
            raise e

    async def _generate_response(self, query: str, context_chunks: List[dict]) -> str:
        """
        Generate a response based on the query and context chunks.

        Args:
            query: The user's query
            context_chunks: List of relevant chunks from the textbook

        Returns:
            Generated response string
        """
        # Prepare messages for the chat service
        messages = [
            {"role": "user", "content": query}
        ]

        # Generate response using the chat service
        response = await self.chat_service.generate_response(messages, context_chunks)
        return response

    def _calculate_confidence_score(self, relevant_chunks: List[dict], query: str, response: str) -> float:
        """
        Calculate a confidence score for the response based on various factors.

        Args:
            relevant_chunks: List of chunks used to generate the response
            query: The original query
            response: The generated response

        Returns:
            Confidence score between 0.0 and 1.0
        """
        if not relevant_chunks:
            return 0.0

        # Base confidence on the relevance score of the top result
        base_score = relevant_chunks[0].get('score', 0.5)  # Default to 0.5 if no score available

        # Adjust based on number of relevant chunks found
        num_chunks = len(relevant_chunks)
        if num_chunks >= 3:
            chunk_factor = 1.0
        elif num_chunks == 2:
            chunk_factor = 0.8
        else:  # num_chunks == 1
            chunk_factor = 0.6

        # Adjust based on response length (longer responses might indicate more confidence)
        response_length_factor = min(len(response) / 200, 1.0)  # Cap at 1.0

        # Combine factors
        confidence = base_score * chunk_factor * response_length_factor

        # Ensure confidence is between 0 and 1
        return max(0.0, min(1.0, confidence))