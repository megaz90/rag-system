import argparse
import sys

from src.ingest import document_indexer
from src.query import rag_querier


def handle_search(args) -> None:
    """
    Handles the 'search' command.

    This function:
    - Takes user query from CLI
    - Searches vector database
    - Prints raw retrieved documents with metadata (no LLM response)
    """
    if not args.query:
        print("Error: Please provide a query with -q or --query")
        sys.exit(1)

    print("-" * 60)
    print(f"Searching for : {args.query}")
    print("-" * 60)
    results = rag_querier.search_database(args.query, args.top_k)

    if not results["documents"][0]:
        print("-" * 60)
        print("No results found.")
        print("-" * 60)
        return

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0] if "distances" in results else None

    print(f"\nFound {len(documents)} results:\n")

    for i, (doc, meta) in enumerate(zip(documents, metadatas), 1):
        score = f" (distance: {distances[i-1]:.3f})" if distances else ""
        print(f"{i}. From: {meta['source']}{score}")
        print(f"   {doc[:300]}...")
        print()


def handle_question(args) -> None:
    """
    Handles the 'query' command.

    This function:
    - Sends user query to RAG pipeline
    - Retrieves context + generates LLM answer
    """
    if not args.question:
        print("Error: Please provide a query with -q or --question")
        sys.exit(1)

    rag_querier.ask_question(args.question)


def handle_index() -> None:
    """
    Handles the 'index' command.

    This function:
    - Reads documents from disk
    - Chunks them
    - Embeds them
    - Stores them in vector DB (ChromaDB)
    """
    document_indexer.build_index()


def main() -> None:
    """
    Entry point for CLI application.

    Responsibilities:
    - Define CLI structure using argparse
    - Register subcommands
    - Route commands to correct handler
    """
    parser = argparse.ArgumentParser(
        description="RAG System - Retrieval-Augmented Generation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
    Examples:
    python main.py index                          # Build index from documents
    python main.py ask -q "What is the warranty?"  # Ask a question
    python main.py interactive                    # Interactive mode
    python main.py search -q "returns"            # Search without answering
    python main.py stats                          # Show database info
    python main.py reset                          # Clear the database
            """,
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    index_parser = subparsers.add_parser("index", help="Build document index")
    index_parser.add_argument(
        "--documents-path",
        default="./data/documents",
        help="Path to documents folder (default: ./data/documents)",
    )

    # Query command
    query_parser = subparsers.add_parser("ask", help="Ask a question")
    query_parser.add_argument(
        "-q", "--question", type=str, help="Question to ask", required=True
    )
    query_parser.add_argument(
        "-k", "--top-k", type=int, default=3, help="Number of docs to retrieve"
    )

    # Search command
    search_parser = subparsers.add_parser("search", help="Search documents only")
    search_parser.add_argument("-q", "--query", type=str, help="Search query")
    search_parser.add_argument(
        "-k", "--top-k", type=int, default=3, help="Number of results"
    )

    # Parse arguments
    args = parser.parse_args()

    if args.command == "index":
        handle_index()
    elif args.command == "ask":
        handle_question(args)
    elif args.command == "search":
        handle_search(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
