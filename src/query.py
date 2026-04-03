from typing import Any, List

from src.core.llm.llm_chat_models import OllamaChatModel
from src.query_translator import QueryTranslator


class RAGQuerier:
    def __init__(self):
        pass

    def generate_answer(self, query: str, context_docs: List[Any]) -> str:
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

    def query_translation_pipeline(self, query: str) -> List[str]:
        """ """
        translator_docs = QueryTranslator().multi_query_translator(query)

        return [doc["text"] for doc in translator_docs]

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

        documents = self.query_translation_pipeline(query)

        answer = self.generate_answer(query, documents)

        print("\n" + "-" * 60)
        print("Answer:")
        print("-" * 60)
        print(answer)
        print("-" * 60)


rag_querier = RAGQuerier()
