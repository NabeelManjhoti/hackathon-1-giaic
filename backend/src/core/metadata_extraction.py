import re
from typing import Dict, Any, List, Optional
from pathlib import Path


class MetadataExtractor:
    """
    Service for extracting metadata from textbook content.
    """

    @staticmethod
    def extract_from_text(content: str, title: str = None) -> Dict[str, Any]:
        """
        Extract metadata from textbook content.

        Args:
            content: The textbook content
            title: Optional title to include in metadata

        Returns:
            Dictionary containing extracted metadata
        """
        metadata = {
            'title': title or 'Unknown Title',
            'word_count': len(content.split()),
            'character_count': len(content),
            'page_count_estimate': len(content) // 2000,  # Rough estimate (2000 chars per page)
            'chapters': [],
            'sections': [],
            'has_diagrams': False,
            'has_tables': False,
            'language': 'en',  # Default to English
        }

        # Extract chapter information
        chapters = MetadataExtractor._extract_chapters(content)
        metadata['chapters'] = chapters

        # Extract section information
        sections = MetadataExtractor._extract_sections(content)
        metadata['sections'] = sections

        # Check for diagrams and tables
        metadata['has_diagrams'] = bool(re.search(r'(figure|diagram|chart|graph)', content, re.IGNORECASE))
        metadata['has_tables'] = bool(re.search(r'(table|fig\.)', content, re.IGNORECASE))

        return metadata

    @staticmethod
    def _extract_chapters(content: str) -> List[Dict[str, Any]]:
        """
        Extract chapter information from content.

        Args:
            content: The textbook content

        Returns:
            List of chapter information
        """
        # Look for common chapter patterns
        chapter_patterns = [
            r'(?:^|\n)Chapter\s+(\d+)[\s:\-\.\n]+([^\n]{1,100})',
            r'(?:^|\n)(\d+)\.\s*([A-Z][^\n]{1,100})',  # E.g., "1. Introduction"
            r'(?:^|\n)Part\s+(\d+)[\s:\-\.\n]+([^\n]{1,100})',
        ]

        chapters = []
        for pattern in chapter_patterns:
            matches = re.finditer(pattern, content, re.IGNORECASE)
            for match in matches:
                chapter_num = match.group(1)
                chapter_title = match.group(2).strip()
                chapters.append({
                    'number': chapter_num,
                    'title': chapter_title,
                    'start_pos': match.start()
                })

        # Sort chapters by position in the text
        chapters.sort(key=lambda x: x['start_pos'])
        return chapters

    @staticmethod
    def _extract_sections(content: str) -> List[Dict[str, Any]]:
        """
        Extract section information from content.

        Args:
            content: The textbook content

        Returns:
            List of section information
        """
        # Look for common section patterns
        section_patterns = [
            r'(?:^|\n)([0-9]+(?:\.[0-9]+)*)\s+([A-Z][^\n]{1,100})',  # E.g., "1.1 Introduction"
            r'(?:^|\n)Section\s+([0-9]+(?:\.[0-9]+)*)[\s:\-\.\n]+([^\n]{1,100})',
            r'(?:^|\n)##\s+([^\n]{1,100})',  # Markdown-style headers
            r'(?:^|\n)#\s+([^\n]{1,100})',  # Markdown-style main headers
        ]

        sections = []
        for pattern in section_patterns:
            matches = re.finditer(pattern, content)
            for match in matches:
                if len(match.groups()) >= 2:
                    section_id = match.group(1)
                    section_title = match.group(2).strip()
                else:
                    section_id = f"section_{len(sections)+1}"
                    section_title = match.group(1).strip()

                sections.append({
                    'id': section_id,
                    'title': section_title,
                    'start_pos': match.start()
                })

        # Sort sections by position in the text
        sections.sort(key=lambda x: x['start_pos'])
        return sections

    @staticmethod
    def extract_from_file(file_path: str, title: str = None) -> Dict[str, Any]:
        """
        Extract metadata from a textbook file.

        Args:
            file_path: Path to the textbook file
            title: Optional title to include in metadata

        Returns:
            Dictionary containing extracted metadata
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            return MetadataExtractor.extract_from_text(content, title)
        except Exception as e:
            print(f"Error extracting metadata from {file_path}: {e}")
            return {
                'title': title or Path(file_path).stem,
                'error': str(e)
            }