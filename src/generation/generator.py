from typing import List

from src.core.llm.factory import llm_provider


class LLMResponseGenerator:
    def generate_answer(self, query: str, context_docs: List[str]) -> str:
        """
        Generate a final answer using the LLM based on retrieved context.

        Steps:
        - Combine retrieved chunks into a single context
        - Build a prompt with instruction + context + question
        - Send to LLM model
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

        response = llm_provider().generate(prompt)

        return response.message.content
