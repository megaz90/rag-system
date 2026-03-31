from chunk import markdown_text_chunking
from pathlib import Path

import chromadb
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


def search_database(query: str, top_result: int = 1):
    """
    Search for documents similar to the query.

    query: the user's question
    top_result: how many results to return
    """
    query_embeddings = embedding_model.encode([query])[0].tolist()

    result = collection.query(query_embeddings=query_embeddings, n_results=top_result)

    print(result["documents"])


# def generate_answer(query, context_docs):
#     """
#     Use GPT to generate an answer based on retrieved documents.
    
#     query: the user's question
#     context_docs: list of relevant text chunks
#     """
#     # Combine all context documents
#     context = "\n\n".join(context_docs)
    
#     # Create the prompt
#     prompt = f"""Answer the question based on the context below. If the answer cannot be found in the context, say 
#     "I don't have enough information to answer that."
#     Context:
#     {context}

#     Question: {query}

#     Answer:"""
    
#     # Get response from GPT
#     response = client.chat.completions.create(
#         model="gpt-4",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant that answers questions based on the provided context."},
#             {"role": "user", "content": prompt}
#         ],
#         temperature=0  # Make it deterministic
#     )
    
#     return response.choices[0].message.content


markdown_text = Path("docs/ims-manual.md").read_text(encoding="utf-8")

chunked_text = markdown_text_chunking(markdown_text)

add_documents(
    chunked_text,
    [f"id-{i}" for i in range(len(chunked_text))],
)

# text = "Artificial intelligence has become one of the most transformative technologies of the modern era, influencing nearly every aspect of human life, from healthcare and education to transportation and entertainment. At its core, artificial intelligence refers to the ability of machines to perform tasks that typically require human intelligence, such as understanding language, recognizing patterns, solving problems, and making decisions. One of the key drivers behind the rapid advancement of AI is the development of machine learning, a subset of AI that enables systems to learn from data rather than being explicitly programmed. Instead of writing rigid rules for every possible scenario, developers train models on large datasets, allowing them to identify patterns and make predictions based on new inputs. This approach has led to breakthroughs in areas like image recognition, natural language processing, and recommendation systems. For example, in healthcare, AI systems can analyze medical images such as X-rays or MRIs with remarkable accuracy, sometimes matching or even exceeding human specialists in detecting diseases like cancer. In education, AI-powered tools can personalize learning experiences by adapting content to the needs and progress of individual students, helping them learn at their own pace. In transportation, self-driving car technology relies heavily on AI algorithms to interpret sensor data, detect obstacles, and make real-time driving decisions. Companies like Tesla and Waymo are actively working on autonomous systems that could reshape the future of mobility. Meanwhile, in entertainment, platforms like Netflix and YouTube use AI-driven recommendation engines to suggest content based on user behavior, ensuring a more engaging experience. Despite these benefits, AI also raises important ethical and societal questions, such as job displacement, privacy concerns, and the potential misuse of autonomous systems. As AI continues to evolve, it becomes increasingly important to balance innovation with responsibility, ensuring that these technologies are developed and used in ways that benefit humanity as a whole. The internet has fundamentally changed the way people communicate, access information, and conduct business. Since its widespread adoption in the late 20th century, it has grown from a simple network connecting a few computers into a global infrastructure that supports billions of devices. Today, the internet enables instant communication through email, messaging apps, and video conferencing platforms, allowing people to stay connected regardless of geographical distance. Social media platforms such as Facebook, Instagram, and Twitter have further transformed communication by enabling users to share thoughts, images, and videos with a global audience in real time. This has not only changed personal communication but has also had a profound impact on politics, journalism, and marketing. In the business world, the internet has enabled the rise of e-commerce, allowing companies to sell products and services online without the need for physical storefronts. Giants like Amazon and Alibaba have built massive global operations by leveraging online marketplaces and logistics networks. Small businesses have also benefited, as the internet provides access to a much larger customer base than traditional methods would allow. Additionally, digital marketing techniques such as search engine optimization (SEO), social media advertising, and email campaigns have become essential tools for reaching and engaging customers. However, the increasing reliance on the internet also brings challenges, including cybersecurity threats, misinformation, and data privacy issues. Cyberattacks such as phishing, ransomware, and data breaches can cause significant financial and reputational damage to individuals and organizations. Misinformation spreads rapidly online, sometimes influencing public opinion and even election outcomes. As a result, governments, companies, and individuals must work together to create safer and more trustworthy digital environments. Looking ahead, emerging technologies like 5G, cloud computing, and the Internet of Things (IoT) are expected to further expand the capabilities of the internet, enabling even more connected and intelligent systems across industries."

search_database("cash account")


