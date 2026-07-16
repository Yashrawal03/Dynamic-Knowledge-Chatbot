from utils.loader import load_text
from utils.vectordb import create_vector_db

documents = load_text()

create_vector_db(documents)

print("Vector Database Created")