from typing import Any, Dict, List

from ollama import ChatResponse, chat

from src.core.config import MODEL_NAME
from src.core.database import db


def search_database(query: str, top_result: int = 3) -> Dict[str, Any]:
    """
    Retrieve the most similar document chunks from the vector database.

    Steps:
    - Convert query into embedding
    - Query ChromaDB using cosine similarity
    - Return top matching chunks
    """
    query_embeddings = db.embedding_model.encode([query])[0].tolist()
    collection = db.get_or_create_collection()

    return collection.query(query_embeddings=query_embeddings, n_results=top_result)


def generate_answer(query: str, context_docs: List[str]) -> str:
    """
    Generate a final answer using the LLM based on retrieved context.

    Steps:
    - Combine retrieved chunks into a single context
    - Build a prompt with instruction + context + question
    - Send to Ollama model
    - Return generated response
    """
    # Combine all context documents
    context = "\n\n".join(context_docs)

    # Create the prompt
    prompt = f"""Answer the question based on the context below. If the answer cannot be found in the context, say
    "I don't have enough information to answer that."
    Context:
    {context}

    Question: {query}

    Answer:"""

    response: ChatResponse = chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that answers questions based on the provided context.",
            },
            {"role": "user", "content": prompt},
        ],
    )

    return response.message.content


def ask_question(query: str) -> None:
    """
    End-to-end RAG pipeline:

    1. Accept user question
    2. Retrieve relevant chunks from vector DB
    3. Send chunks + question to LLM
    4. Print final answer
    """
    print("-" * 60)
    print("Question: ", query)
    print("-" * 60)

    results = search_database(query)

    documents = results.get("documents", [[]])[0]

    # Edge case: no results
    if not documents:
        print("No relevant context found.")
        return

    answer = generate_answer(query, documents)

    print("\n" + "-" * 60)
    print("Answer:")
    print("-" * 60)
    print(answer)
    print("-" * 60)
