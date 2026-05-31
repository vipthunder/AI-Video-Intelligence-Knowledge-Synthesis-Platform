from operator import itemgetter

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from src.llm import llm

def format_docs(docs):
    formatted = []

    for doc in docs:
        source = doc.metadata.get("video_name", "Unknown")
        start = doc.metadata.get("start_time", 0)
        end = doc.metadata.get("end_time", 0)

        formatted.append(
            f"""
SOURCE: {source}
TIMESTAMP: {start:.2f}s - {end:.2f}s

CONTENT:
{doc.page_content}
"""
        )

    return "\n\n".join(formatted)
    

def create_rag_chain(retriever):

    prompt = ChatPromptTemplate.from_template(
        """You are an AI Video Intelligence Assistant.

Use ONLY the provided context.

When answering:

1. Mention which video the information came from.
2. Mention timestamps whenever available.
3. If information comes from multiple videos, compare them.
4. If no answer exists, say so.

Context:
{context}

Question:
{question}

        
        """
    )

    rag_chain = (
        {
            "context":
                itemgetter("question")| retriever| format_docs,   # chain

            "question":
                itemgetter("question")
        }
        | prompt| llm | StrOutputParser()
    )

    return rag_chain
    

def retrieve_with_sources(retriever, question):

    docs = retriever.invoke(question)

    sources = []

    for doc in docs:
        sources.append({
            "video": doc.metadata.get("video_name"),
            "start": doc.metadata.get("start_time"),
            "end": doc.metadata.get("end_time")
        })

    return docs, sources
