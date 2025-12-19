from typing import List, Dict, Any
from ..core.vector_store import VectorStore
from ..services.embedding_service import EmbeddingService


class IndexingService:
    """
    Service for indexing textbook content into the vector store.
    """

    def __init__(self, vector_store: VectorStore, embedding_service: EmbeddingService):
        self.vector_store = vector_store
        self.embedding_service = embedding_service

    async def index_chunks(self, chunks: List[Dict[str, Any]]) -> bool:
        """
        Index pre-processed text chunks into the vector store.

        Args:
            chunks: List of chunks with text and metadata

        Returns:
            True if indexing was successful, False otherwise
        """
        try:
            # Prepare chunks for vector store ingestion
            processed_chunks = []
            for chunk in chunks:
                # Create embedding for the chunk text
                embedding = await self.embedding_service.create_embedding(chunk['text'])

                processed_chunk = {
                    'id': chunk.get('id', f"chunk_{len(processed_chunks)}"),
                    'text': chunk['text'],
                    'embedding': embedding,
                    'metadata': chunk.get('metadata', {})
                }
                processed_chunks.append(processed_chunk)

            # Add chunks to vector store
            self.vector_store.add_text_chunks(processed_chunks)
            return True
        except Exception as e:
            print(f"Error indexing chunks: {e}")
            return False

    def validate_chunks(self, chunks: List[Dict[str, Any]]) -> bool:
        """
        Validate that the chunks meet quality criteria.

        Args:
            chunks: List of chunks to validate

        Returns:
            True if chunks are valid, False otherwise
        """
        if not chunks:
            return False

        for chunk in chunks:
            if 'text' not in chunk or not chunk['text'].strip():
                return False

        return True