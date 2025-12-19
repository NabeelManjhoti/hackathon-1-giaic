import asyncio
from typing import List, Dict, Any
from ..core.vector_store import VectorStore
from ..services.embedding_service import EmbeddingService
from ..core.chunking import chunk_text


class IngestionService:
    """
    Service for ingesting textbook content into the vector store.
    """

    def __init__(self, vector_store: VectorStore, embedding_service: EmbeddingService):
        self.vector_store = vector_store
        self.embedding_service = embedding_service

    async def ingest_textbook(self, title: str, content: str, metadata: Dict[str, Any] = None) -> bool:
        """
        Ingest a textbook into the vector store.

        Args:
            title: Title of the textbook
            content: Full content of the textbook
            metadata: Additional metadata about the textbook

        Returns:
            True if ingestion was successful, False otherwise
        """
        if metadata is None:
            metadata = {}

        # Chunk the textbook content
        chunks = chunk_text(content)

        # Prepare chunks for ingestion
        processed_chunks = []
        for i, chunk in enumerate(chunks):
            # Create embedding for the chunk
            embedding = await self.embedding_service.create_embedding(chunk)

            # Prepare the chunk for storage
            processed_chunk = {
                'id': f"{title.replace(' ', '_').lower()}_chunk_{i}",
                'text': chunk,
                'embedding': embedding,
                'metadata': {
                    **metadata,
                    'source': title,
                    'chunk_index': i,
                    'total_chunks': len(chunks)
                }
            }
            processed_chunks.append(processed_chunk)

        # Add chunks to vector store
        try:
            self.vector_store.add_text_chunks(processed_chunks)
            return True
        except Exception as e:
            print(f"Error ingesting textbook: {e}")
            return False

    async def ingest_from_file(self, file_path: str, title: str, metadata: Dict[str, Any] = None) -> bool:
        """
        Ingest textbook content from a file.

        Args:
            file_path: Path to the textbook file
            title: Title of the textbook
            metadata: Additional metadata about the textbook

        Returns:
            True if ingestion was successful, False otherwise
        """
        # For now, we'll simulate reading from a text file
        # In a real implementation, you'd handle different file formats (PDF, etc.)
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            return await self.ingest_textbook(title, content, metadata)
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")
            return False