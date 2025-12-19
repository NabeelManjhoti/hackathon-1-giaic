from typing import List, Dict, Any
from ..models.response import Reference
from ..core.vector_store import VectorStore


class ReferenceService:
    """
    Service for extracting and managing references to textbook sections.
    """

    def __init__(self, vector_store: VectorStore):
        self.vector_store = vector_store

    def create_references_from_chunks(self, chunks: List[Dict[str, Any]]) -> List[Reference]:
        """
        Create reference objects from retrieved text chunks.

        Args:
            chunks: List of retrieved chunks from the vector store

        Returns:
            List of Reference objects
        """
        references = []
        for chunk in chunks:
            # Extract reference information from chunk metadata
            metadata = chunk.get('metadata', {})

            reference = Reference(
                source=metadata.get('source', 'textbook'),
                page_number=metadata.get('page_number', 1),
                section=metadata.get('section', 'Unknown Section'),
                text_preview=chunk.get('content', '')[:100] + "..." if len(chunk.get('content', '')) > 100 else chunk.get('content', '')
            )
            references.append(reference)

        return references

    def validate_references(self, references: List[Reference]) -> bool:
        """
        Validate that the references meet quality criteria.

        Args:
            references: List of references to validate

        Returns:
            True if references are valid, False otherwise
        """
        # Ensure we have at least one reference
        if len(references) == 0:
            return False

        # Check that all references have required fields
        for ref in references:
            if not ref.source or not ref.section:
                return False

        return True

    def rank_references_by_relevance(self, references: List[Reference], query: str) -> List[Reference]:
        """
        Rank references by their relevance to the query.
        In a real implementation, this would use more sophisticated ranking algorithms.

        Args:
            references: List of references to rank
            query: The original query for context

        Returns:
            List of references ranked by relevance
        """
        # For now, return the references as-is
        # In a real implementation, we would implement relevance ranking
        return references