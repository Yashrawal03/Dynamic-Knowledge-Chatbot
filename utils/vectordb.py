from langchain_chroma import Chroma
from utils.embedding import embedding
from config import VECTOR_DB

def create_vector_db(documents):

    db = Chroma.from_documents(
        documents,
        embedding,
        persist_directory=VECTOR_DB
    )

    return db