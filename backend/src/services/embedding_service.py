import openai
from typing import List
from ..core.config import settings


class EmbeddingService:
    """
    Service for generating embeddings using OpenAI's text-embedding-3-small model.
    """

    def __init__(self):
        openai.api_key = settings.openai_api_key

    async def create_embedding(self, text: str) -> List[float]:
        """
        Create a single embedding for the given text.

        Args:
            text: The text to embed

        Returns:
            List of floats representing the embedding vector
        """
        response = await openai.Embedding.acreate(
            input=text,
            model="text-embedding-3-small"
        )
        return response['data'][0]['embedding']

    async def create_embeddings(self, texts: List[str]) -> List[List[float]]:
        """
        Create embeddings for multiple texts.

        Args:
            texts: List of texts to embed

        Returns:
            List of embedding vectors
        """
        if len(texts) == 0:
            return []

        # Batch embeddings for efficiency (OpenAI allows up to 2048 texts per request)
        response = await openai.Embedding.acreate(
            input=texts,
            model="text-embedding-3-small"
        )

        return [item['embedding'] for item in response['data']]