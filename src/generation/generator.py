from src.core.llm.factory import llm_provider
from src.prompts.system_prompts import DEFAULT_SYSTEM_PROMPT


class LLMResponseGenerator:
    def generate_answer(
        self, user_prompt: str, system_prompt: str = DEFAULT_SYSTEM_PROMPT
    ) -> str:
        """
        Generate a final answer using the LLM based on retrieved context.

        Steps:
        - Build a prompt with instruction + context + question
        - Send to LLM model
        - Return generated response
        """

        response = llm_provider(system_prompt=system_prompt).generate(user_prompt)

        return response.message.content
