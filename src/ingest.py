from datetime import datetime
from pathlib import Path

from src.chunker import markdown_text_chunking, plain_text_chunking
from src.core.database import db
from src.core.utils import get_content_hash


def retrieve_documents():
    BASE_DIR = Path(__file__).resolve().parent.parent
    accepted_extensions = [".txt", ".md"]
    files = Path(BASE_DIR / "data/documents").rglob("*")
    docs = []
    for doc in files:
        if doc.suffix in accepted_extensions:
            docs.append(
                {
                    "name": doc.name,
                    "path": str(doc),
                    "text": doc.read_text(encoding="utf-8"),
                    "type": doc.suffix,
                }
            )

    print("-" * 60)
    print(f"Retrieved {len(docs)} documents from data/documents/")
    print("-" * 60)
    return docs


def get_indexed_documents(collection, text: str):
    """Get list of already indexed documents where the source file has been updated"""
    try:
        results = collection.get()

        # Extract unique source files
        updated_indexed_docs = set()
        unchanged_indexed_docs = set()

        for meta in results.get("metadatas", []):
            if (
                meta
                and "file_hash" in meta
                and meta["file_hash"] != get_content_hash(text)
            ):
                updated_indexed_docs.add(meta["source"])
            else:
                unchanged_indexed_docs.add(meta["source"])

        return updated_indexed_docs, unchanged_indexed_docs
    except Exception as e:
        print("An error occurred:", str(e))
        return set()


def build_index(collection_name: str) -> None:

    collection = db.chroma_client.get_or_create_collection(name=collection_name)

    docs = retrieve_documents()

    # Track statistics
    skipped_docs = 0
    processed_docs = 0

    for doc in docs:
        # Skip if already indexed and not updated
        changed_indexed_docs, unchanged_docs = get_indexed_documents(
            collection, doc["text"]
        )

        if doc["name"] in unchanged_docs:
            print(f"Skipping {doc['name']} (already indexed)")
            skipped_docs += 1
            continue

        collection.delete(where={"file_name": doc["name"]})

        print(f"Processing: {doc['name']}")

        if doc["type"] == ".txt":
            chunks = plain_text_chunking(doc["text"])
        elif doc["type"] == ".md":
            chunks = markdown_text_chunking(doc["text"])
        else:
            continue

        if not chunks:
            print(
                f"No chunks created from {doc['name']}. The document is probably empty."
            )
            continue

        embeddings = db.embedding_model.encode(chunks).tolist()

        collection.upsert(
            documents=chunks,
            ids=[f"{doc['name']}_chunk_{i}" for i in range(len(chunks))],
            embeddings=embeddings,
            metadatas=[
                {
                    "source": doc["name"],
                    "source_path": doc["path"],
                    "chunk_id": i,
                    "file_type": doc["type"],
                    "file_hash": get_content_hash(doc["text"]),
                    "indexed_at": datetime.now().isoformat(),
                    "total_chunks": len(chunks),
                }
                for i in range(len(chunks))
            ],
        )
        print(f"Added {len(chunks)} chunks to the database from {doc['name']}")

    # Summary
    print("\n" + "=" * 60)
    print("Indexing Summary:")
    print(f"  • New documents processed: {processed_docs}")
    print(f"  • Documents skipped: {skipped_docs}")
    print(f"  • Total chunks in index: {collection.count()}")
    print("=" * 60)
