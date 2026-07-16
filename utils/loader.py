from langchain_community.document_loaders import TextLoader
from config import TEXT_FILE

def load_text():

    loader = TextLoader(TEXT_FILE)

    return loader.load()