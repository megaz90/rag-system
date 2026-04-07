from datetime import datetime
from pathlib import Path
from typing import List, TypedDict

from src.core.database import db
from src.core.embeddings import vector_embedding
from src.core.utils import get_content_hash
from src.ingestion.chunker import markdown_text_chunking, plain_text_chunking


class Document(TypedDict):
    name: str
    path: str
    text: str
    category: str
    type: str


class DocumentIndexer:
    def _retrieve_documents(self) -> List[Document]:
        """
        Reads all supported documents from the data folder.

        Supported formats:
        - .txt
        - .md

        Returns:
            List of Document dictionaries containing:
            - file name
            - full file path
            - raw text content
            - file type
        """
        BASE_DIR = Path(__file__).resolve().parents[2]
        accepted_extensions = [".txt", ".md"]
        files = Path(BASE_DIR / "data/documents").rglob("*")
        docs = []
        for doc in files:
            if doc.suffix in accepted_extensions:
                doc_folder = doc.parent.name
                category_name = doc_folder.replace("_docs", "")
                docs.append(
                    {
                        "name": doc.name,
                        "path": str(doc),
                        "category": category_name,
                        "type": doc.suffix,
                        "text": doc.read_text(encoding="utf-8"),
                    }
                )

        print("-" * 60)
        print(f"Retrieved {len(docs)} documents from data/documents/")
        print("-" * 60)
        return docs

    def build_index(self) -> None:
        """
        Main ingestion pipeline for RAG system.

        Workflow:
        1. Load documents from disk
        2. Check if they are already indexed
        3. Skip unchanged files
        4. Delete outdated chunks
        5. Chunk document
        6. Generate embeddings
        7. Store in ChromaDB
        """
        collection = db.get_or_create_collection()

        docs = self._retrieve_documents()

        # Track statistics
        skipped_docs = 0
        processed_docs = 0

        for doc in docs:
            file_hash = get_content_hash(doc["text"])

            existing = collection.get(where={"source": doc["name"]})

            if existing["metadatas"]:
                old_hash = existing["metadatas"][0]["file_hash"]

                if old_hash == file_hash:
                    print(f"Skipping {doc['name']} (unchanged)")
                    skipped_docs += 1
                    continue

                collection.delete(where={"source": doc["name"]})

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
            else:
                processed_docs += 1

            embeddings = vector_embedding.embedding_model.encode(chunks).tolist()

            collection.upsert(
                documents=chunks,
                ids=[f"{doc['name']}_chunk_{i}" for i in range(len(chunks))],
                embeddings=embeddings,
                metadatas=[
                    {
                        "source": doc["name"],
                        "source_path": doc["path"],
                        "chunk_id": i,
                        "category": doc["category"],
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


document_indexer = DocumentIndexer()
