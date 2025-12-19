from typing import List, Optional
from qdrant_client import QdrantClient
from qdrant_client.http import models
from qdrant_client.http.models import PointStruct, VectorParams, Distance
from ..core.config import settings


class VectorStore:
    """
    Qdrant vector store client wrapper for textbook content storage and retrieval.
    """

    def __init__(self):
        self.client = QdrantClient(
            url=settings.qdrant_url,
            api_key=settings.qdrant_api_key,
            # Prefer gRPC for better performance
            prefer_grpc=True
        )
        self.collection_name = "textbook_content"
        self.vector_size = 1536  # For OpenAI embeddings

    def create_collection(self):
        """
        Create the collection for storing textbook content if it doesn't exist.
        """
        try:
            self.client.get_collection(self.collection_name)
        except:
            # Collection doesn't exist, create it
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(
                    size=self.vector_size,
                    distance=Distance.COSINE
                )
            )

    def add_text_chunks(self, chunks: List[dict]):
        """
        Add text chunks to the vector store with their embeddings.

        Args:
            chunks: List of dictionaries containing 'id', 'text', 'metadata'
        """
        points = []
        for chunk in chunks:
            points.append(PointStruct(
                id=chunk['id'],
                vector=chunk['embedding'],
                payload={
                    'content': chunk['text'],
                    'metadata': chunk.get('metadata', {})
                }
            ))

        self.client.upsert(
            collection_name=self.collection_name,
            points=points
        )

    def search(self, query_embedding: List[float], top_k: int = 5) -> List[dict]:
        """
        Search for similar content in the vector store.

        Args:
            query_embedding: The embedding vector to search for
            top_k: Number of results to return

        Returns:
            List of matching chunks with content and metadata
        """
        results = self.client.search(
            collection_name=self.collection_name,
            query_vector=query_embedding,
            limit=top_k
        )

        return [
            {
                'id': result.id,
                'content': result.payload['content'],
                'metadata': result.payload['metadata'],
                'score': result.score
            }
            for result in results
        ]

    def close(self):
        """
        Close the connection to the vector store.
        """
        if hasattr(self.client, 'close'):
            self.client.close()