from typing import List


def plain_text_chunking(
    text: str, chunk_size: int = 500, overlap: int = 50
) -> List[str]:
    """
    Splits a large text into smaller overlapping chunks for use in embedding-based retrieval systems (e.g., RAG).

    The function attempts to preserve semantic meaning by avoiding arbitrary cuts. Instead of strictly splitting at the
    chunk_size limit, it tries to find a natural breakpoint (such as the last occurrence of a period ".") within the
    boundary to end a chunk cleanly.

    Overlap is used between consecutive chunks to ensure that important context is not lost at chunk boundaries,
    improving retrieval quality and coherence in downstream tasks.

    Args:
        text (str): The input text to be chunked.
        chunk_size (int): Maximum size of each chunk.
        overlap (int): Number of characters/tokens to overlap between consecutive chunks.

    Returns:
        List[str]: A list of text chunks ready for embedding generation.
    """
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]

        if end < len(text):
            # Finds last occurrence index of "."
            last_period = chunk.rfind(".")
            if last_period != -1:
                sentence_end_index = last_period + 1
                # Update the slicing according to sentence ending
                chunk = chunk[:sentence_end_index]
                # Update the end according to new slicing to assign correct start position for next chunk
                end = start + sentence_end_index

        chunks.append(chunk)
        start = end - overlap

    return chunks


def markdown_text_chunking(
    markdown_text: str, min_tokens: int = 120, max_tokens: int = 400
) -> List[str]:
    """
    Smart markdown chunking strategy that:

    - Preserves document structure (headings)
    - Keeps chunks within size limits
    - Combines small sections
    - Splits large sections into smaller pieces
    """
    import re

    # First, split by ## headings
    sections = re.split(r"\n(?=## )", markdown_text)

    chunks = []
    current_group = []
    current_size = 0

    # Extract the main # heading
    main_heading = ""
    if sections[0].startswith("# "):
        main_heading = sections[0].split("\n")[0]
        sections[0] = "\n".join(sections[0].split("\n")[1:])

    for section in sections:
        section = section.strip()  # Clear whitespaces
        if not section:
            continue

        # Count tokens (rough estimate: words)
        section_tokens = len(section.split())

        # Case 1: Section is too large - split it
        if section_tokens > max_tokens:
            # Save any accumulated small sections first
            if current_group:
                chunk_text = main_heading + "\n\n" + "\n\n".join(current_group)
                chunks.append(chunk_text)
                current_group = []
                current_size = 0

            # Split large section by paragraphs
            paragraphs = section.split("\n\n")

            heading = paragraphs[0] if paragraphs[0].startswith("##") else ""

            temp_chunk = [heading] if heading else []
            temp_size = 0

            for para in paragraphs[1:] if heading else paragraphs:
                para_tokens = len(para.split())

                # Checking if the current paragraph is not greater than max_tokens
                if temp_size + para_tokens > max_tokens and temp_chunk:
                    # Save chunk
                    chunk_text = main_heading + "\n\n" + "\n\n".join(temp_chunk)
                    chunks.append(chunk_text)
                    temp_chunk = [heading] if heading else []
                    temp_size = 0

                temp_chunk.append(para)
                temp_size += para_tokens

            # Save remaining
            if temp_chunk:
                chunk_text = main_heading + "\n\n" + "\n\n".join(temp_chunk)
                chunks.append(chunk_text)

        # Case 2: Section is small - try to combine with others
        elif section_tokens < min_tokens:
            current_group.append(section)
            current_size += section_tokens

            # If combined size is good, save it
            if current_size >= min_tokens:
                chunk_text = main_heading + "\n\n" + "\n\n".join(current_group)
                chunks.append(chunk_text)
                current_group = []
                current_size = 0

        # Case 3: Section is just right
        else:
            # Save any accumulated sections first
            if current_group:
                chunk_text = main_heading + "\n\n" + "\n\n".join(current_group)
                chunks.append(chunk_text)
                current_group = []
                current_size = 0

            # Save this section
            chunk_text = main_heading + "\n\n" + section
            chunks.append(chunk_text)

    # Don't forget leftover small sections
    if current_group:
        chunk_text = main_heading + "\n\n" + "\n\n".join(current_group)
        chunks.append(chunk_text)

    return chunks
