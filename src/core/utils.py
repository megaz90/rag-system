import hashlib


def get_content_hash(text: str) -> str:
    """
    Generate hash of document content. This uniquely identifies the content, not the file
    """
    return hashlib.sha256(text.encode("utf-8")).hexdigest()
