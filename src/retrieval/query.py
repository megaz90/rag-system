from typing import List

from src.generation.generator import LLMResponseGenerator
from src.retrieval.query_translator import QueryTranslator
from src.schemas.query_context import QueryContext


class RAGQuerier:
    def query_translation_pipeline(self, context: QueryContext) -> List[str]:
        """
        Translates and expands the user query into multiple reformulated queries and retrieves relevant documents using
        different translation strategies.

        This step improves retrieval quality by generating alternative phrasings of the original query.

        Args:
            context (QueryContext)

        Returns:
            List[str]
        """
        translator_docs = QueryTranslator().rag_fusion_translator(context)

        return [doc["text"] for doc in translator_docs]

    def ask_question(self, context: QueryContext) -> str:
        """
        End-to-end RAG pipeline execution.

        Workflow:
        1. Accepts user query via QueryContext
        2. Expands query and retrieves relevant documents using the translation + RAG fusion pipeline
        3. Passes retrieved context and query to the LLM for final answer generation
        4. Prints the formatted response to stdout

        Args:
            context (QueryContext): Contains the user query and metadata.
        """

        documents = self.query_translation_pipeline(context)

        # Combine all context documents
        docs = "\n\n".join(documents)

        user_prompt = f"""
        Context:
        {docs}

        Question: {context.query}
        """

        print("-" * 60)
        print("Question: ", context.query)
        print("-" * 60)

        answer = LLMResponseGenerator().generate_answer(user_prompt=user_prompt)

        print("\n" + "-" * 60)
        print("Answer:")
        print("-" * 60)
        print(answer)
        print("-" * 60)

        return answer
