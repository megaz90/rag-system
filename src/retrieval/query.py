from typing import List

from src.generation.generator import LLMResponseGenerator
from src.retrieval.query_translator import QueryTranslator


class RAGQuerier:
    def query_translation_pipeline(self, query: str) -> List[str]:
        """ """
        translator_docs = QueryTranslator().rag_fusion_translator(query)

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

        answer = LLMResponseGenerator().generate_answer(query, documents)

        print("\n" + "-" * 60)
        print("Answer:")
        print("-" * 60)
        print(answer)
        print("-" * 60)


rag_querier = RAGQuerier()
