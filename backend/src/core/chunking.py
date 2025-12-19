from typing import List


def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 100) -> List[str]:
    """
    Split text into overlapping chunks.

    Args:
        text: The text to chunk
        chunk_size: Size of each chunk in characters
        overlap: Number of overlapping characters between chunks

    Returns:
        List of text chunks
    """
    if not text:
        return []

    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size

        # If this is the last chunk and it's smaller than chunk_size, include it all
        if end > text_length:
            end = text_length

        chunk = text[start:end]
        chunks.append(chunk)

        # Move start position by chunk_size minus overlap
        start = end - overlap

        # If we're at the end, break to avoid infinite loop
        if start >= text_length:
            break

    # Remove any empty chunks
    chunks = [chunk for chunk in chunks if chunk.strip()]

    return chunks


def chunk_by_sentences(text: str, max_chunk_size: int = 1000) -> List[str]:
    """
    Split text into chunks by sentences, keeping sentences together.

    Args:
        text: The text to chunk
        max_chunk_size: Maximum size of each chunk in characters

    Returns:
        List of text chunks
    """
    import re

    # Split text into sentences
    sentences = re.split(r'[.!?]+\s+', text)
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        # Check if adding this sentence would exceed the max size
        if len(current_chunk + " " + sentence) <= max_chunk_size:
            if current_chunk:
                current_chunk += " " + sentence
            else:
                current_chunk = sentence
        else:
            # If the current chunk is not empty, save it and start a new one
            if current_chunk:
                chunks.append(current_chunk)
            # If the sentence itself is longer than max_chunk_size, we need to split it
            if len(sentence) > max_chunk_size:
                # Split the long sentence into smaller chunks
                sub_chunks = chunk_text(sentence, max_chunk_size, 100)
                chunks.extend(sub_chunks)
                current_chunk = ""
            else:
                current_chunk = sentence

    # Add the last chunk if it's not empty
    if current_chunk:
        chunks.append(current_chunk)

    return chunks