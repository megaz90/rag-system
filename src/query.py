from typing import Any, Dict, List

from src.core.database import db
from src.core.llm.llm_chat_models import OllamaChatModel


class RAGQuerier:
    def __init__(self):
        pass

    def search_database(self, query: str, top_result: int = 3) -> Dict[str, Any]:
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

    def generate_answer(self, query: str, context_docs: List[str]) -> str:
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

        response = OllamaChatModel().generate(prompt)

        return response.message.content

    def ask_question(self, query: str) -> None:
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

        results = self.search_database(query)

        documents = results.get("documents", [[]])[0]

        # Edge case: no results
        if not documents:
            print("No relevant context found.")
            return

        answer = self.generate_answer(query, documents)

        print("\n" + "-" * 60)
        print("Answer:")
        print("-" * 60)
        print(answer)
        print("-" * 60)


rag_querier = RAGQuerier()
