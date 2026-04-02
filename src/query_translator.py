from typing import Any, Dict, List

from src.core.database import db
from src.core.llm.factory import llm_provider


class QueryTranslator:
    """
    First layer of RAG pipeline for transforming user queries to LLM.

    This class contains methods for transforming single user queries with the help of LLM into a format that can be fed
    to the LLM to generate better answers.
    """
    
    def multi_query_translator(self, question: str) -> List[Any]:
        """
        Multi query translator method takes a question from the user and returns a list of alternative questions.
        This is a "Sub-question" strategy which breaks down the user query into multiple questions.
        It goes through following steps:

        1. Generate a prompt for the LLM
        2. Send the prompt to the LLM along with the user query
        3. Return the response from the LLM
        4. Process the response and return a list of alternative questions
        5. Search the vector database using the alternative questions
        6. Returns the unique results so that there are not duplicates
        """
        prompt = f"""You are an AI language model assistant. your task is to generate five different versions of the 
        given user question to retrieve the relevant information from the documents from a vector database. By 
        generating multiple perspectives on the user question, your goal is to help the user overcome some of the 
        limitations of the distance-based similarity search.
        Provide these alternative questions separated by newlines. Original question: {question}"""

        response = llm_provider().generate(prompt)
        
        queries = str(response.message.content).split("\n")
        
        docs = []
        for query in queries if queries else []:
            results = db.search_database(query)
            if not results:
                print("No results returned from DB.")
                continue
            
            documents = results.get("documents")

            if not documents or not isinstance(documents, list):
                print("No documents found.")
                continue
            
            documents = documents[0] if documents and isinstance(documents[0], list) else documents
            
            docs.append(documents)
            
        unique_docs = list(set([doc for doc_list in docs for doc in doc_list]))
        
        return unique_docs

    def rag_fusion_translator(self, question: str):
        prompt = """
        """
        pass
