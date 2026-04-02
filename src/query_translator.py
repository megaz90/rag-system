from src.core.llm.factory import llm_provider


class QueryTranslator:
    """
    First layer of RAG pipeline for transforming user queries to LLM.

    This class contains methods for transforming single user queries with the help of LLM into a format that can be fed
    to the LLM to generate better answers.
    """

    def multi_query_translator(question: str):
        prompt = f"""You are an AI language model assistant. your task is to generate five different versions of the 
        given user question to retrieve the relevant information from the documents from a vector database. By 
        generating multiple perspectives on the user question, your goal is to help the user overcome some of the 
        limitations of the distance-based similarity search.
        Provide these alternative questions separated by newlines. Original question: {question}"""

        response = llm_provider().generate(prompt)

        return response

    def rag_fusion_translator():
        prompt = """
        """
        pass
