from langchain_chroma import Chroma
from src.embedding import embeddings
import uuid


COLLECTION_NAME = "video_knowledge_base"


def create_vector_store(chunks, video_name):
    """
    Add video transcript chunks to ChromaDB.

    Args:
        chunks (list[str]): Text chunks from transcript.
        video_name (str): Original video filename/title.

    Returns:
        Chroma: Chroma vector store instance.
    """

    # Metadata for each chunk
    metadatas = [
        {
            "video_name": video_name,
            "chunk_id": i,
            "start_time": chunk["start"],
            "end_time": chunk["end"]
        }
        for i , chunk in enumerate(chunks)
    ]

    # Unique IDs for each chunk
    ids = [str(uuid.uuid4()) for _ in chunks]

    # Load/Create collection
    vector_store = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory="chroma_db"
    )

    # Add chunks to collection
    vector_store.add_texts(
        texts=[chunk["text"] for chunk in chunks],
        metadatas=metadatas,
        ids=ids
    )

    return vector_store
