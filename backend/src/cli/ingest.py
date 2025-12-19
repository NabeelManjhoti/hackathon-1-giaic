import asyncio
import argparse
from pathlib import Path
from ..core.vector_store import VectorStore
from ..services.embedding_service import EmbeddingService
from ..services.ingestion_service import IngestionService


async def main():
    parser = argparse.ArgumentParser(description="Ingest textbook content into the RAG system")
    parser.add_argument("--file-path", required=True, help="Path to the textbook file")
    parser.add_argument("--title", required=True, help="Title of the textbook")
    parser.add_argument("--source", help="Source identifier for the textbook")
    parser.add_argument("--author", help="Author of the textbook")
    parser.add_argument("--section", help="Section or chapter name")

    args = parser.parse_args()

    # Validate file path
    file_path = Path(args.file_path)
    if not file_path.exists():
        print(f"Error: File {args.file_path} does not exist")
        return

    # Initialize services
    vector_store = VectorStore()
    embedding_service = EmbeddingService()
    ingestion_service = IngestionService(vector_store, embedding_service)

    # Prepare metadata
    metadata = {
        'source': args.source or 'unknown',
        'author': args.author or 'unknown',
        'section': args.section or 'general',
        'file_path': str(file_path)
    }

    print(f"Starting ingestion of {args.title}...")
    success = await ingestion_service.ingest_from_file(
        file_path=str(file_path),
        title=args.title,
        metadata=metadata
    )

    if success:
        print(f"Successfully ingested {args.title} into the vector store")
    else:
        print(f"Failed to ingest {args.title}")

    # Close the vector store connection
    vector_store.close()


if __name__ == "__main__":
    asyncio.run(main())