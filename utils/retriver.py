from langchain_chroma import Chroma
from utils.embedding import embedding
from config import VECTOR_DB

db = Chroma(
    persist_directory=VECTOR_DB,
    embedding_function=embedding
)

retriever = db.as_retriever()

def retrieve(query):

    return retriever.invoke(query)