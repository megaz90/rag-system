from chunk import markdown_text_chunking
from pathlib import Path

import chromadb
from ollama import ChatResponse, chat
from sentence_transformers import SentenceTransformer

chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="test")

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


def add_documents(chunks: list[str], ids: list[str]) -> None:

    embeddings = embedding_model.encode(chunks).tolist()

    collection.add(
        documents=chunks,
        ids=ids,
        embeddings=embeddings,
    )

    print(f"Added {len(chunks)} chunks to the database")


def search_database(query: str, top_result: int = 3):
    """
    Search for documents similar to the query.

    query: the user's question
    top_result: how many results to return
    """
    query_embeddings = embedding_model.encode([query])[0].tolist()

    results = collection.query(query_embeddings=query_embeddings, n_results=top_result)
    
    return results["documents"][0] if results["documents"] else results["documents"]


def generate_answer(query: str, context_docs):
    """
    Use Ollama to generate an answer based on retrieved documents.
    
    query: the user's question
    context_docs: list of relevant text chunks
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
        model='qwen3.5:9b', 
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers questions based on the provided context."},
            {'role': 'user', 'content': prompt},
    ])
    
    return response.message.content

def ask_question(query):
    """
    """
    print(f"Question: ", query)
    print("-" * 50)
    top_docs = search_database(query)
    
    print(generate_answer(query, top_docs))


markdown_text = Path("docs/ims-manual.md").read_text(encoding="utf-8")

chunked_text = markdown_text_chunking(markdown_text)

add_documents(
    chunked_text,
    [f"id-{i}" for i in range(len(chunked_text))],
)


ask_question("How does permissions work?")
