from operator import itemgetter

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from src.llm import llm


def format_docs(docs):
    return "\n\n".join(
        doc.page_content
        for doc in docs
    )


def create_rag_chain(retriever):

    prompt = ChatPromptTemplate.from_template(
        """
        You are an AI assistant.

        Answer the question using only the provided context.

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
