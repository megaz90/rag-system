import argparse

from src.ingest import build_index

# def generate_answer(query: str, context_docs):
#     """
#     Use Ollama to generate an answer based on retrieved documents.

#     query: the user's question
#     context_docs: list of relevant text chunks
#     """
#     # Combine all context documents
#     context = "\n\n".join(context_docs)

#     # Create the prompt
#     prompt = f"""Answer the question based on the context below. If the answer cannot be found in the context, say
#     "I don't have enough information to answer that."
#     Context:
#     {context}

#     Question: {query}

#     Answer:"""

#     response: ChatResponse = chat(
#         model="qwen3.5:9b",
#         messages=[
#             {
#                 "role": "system",
#                 "content": "You are a helpful assistant that answers questions based on the provided context.",
#             },
#             {"role": "user", "content": prompt},
#         ],
#     )

#     return response.message.content


# def ask_question(query):
#     """ """
#     print("Question: ", query)
#     print("-" * 50)
#     top_docs = search_database(query)

#     print(generate_answer(query, top_docs))


def handle_index(args):
    """
    Handles the indexing of the documents
    """
    build_index(args.collection)


# ask_question("How does permissions work?")


def main():
    parser = argparse.ArgumentParser(
        description="RAG System - Retrieval-Augmented Generation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
    Examples:
    python main.py index                          # Build index from documents
    python main.py query -q "What is the warranty?"  # Ask a question
    python main.py interactive                    # Interactive mode
    python main.py search -q "returns"            # Search without answering
    python main.py stats                          # Show database info
    python main.py reset                          # Clear the database
            """,
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    index_parser = subparsers.add_parser("index", help="Build document index")
    index_parser.add_argument(
        "--collection", type=str, help="Collection name", default="RAG"
    )
    index_parser.add_argument(
        "--documents-path",
        default="./data/documents",
        help="Path to documents folder (default: ./data/documents)",
    )

    # Query command
    query_parser = subparsers.add_parser("query", help="Ask a question")
    query_parser.add_argument("-q", "--query", type=str, help="Question to ask")
    query_parser.add_argument(
        "-k", "--top-k", type=int, default=3, help="Number of docs to retrieve"
    )

    # Search command
    search_parser = subparsers.add_parser("search", help="Search documents only")
    search_parser.add_argument("-q", "--query", type=str, help="Search query")
    search_parser.add_argument(
        "-k", "--top-k", type=int, default=5, help="Number of results"
    )

    # Parse arguments
    args = parser.parse_args()

    if args.command == "index":
        handle_index(args)
    elif args.command == "query":
        print("query")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
