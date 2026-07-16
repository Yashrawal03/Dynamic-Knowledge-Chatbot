from bs4 import BeautifulSoup
import requests

from langchain.schema import Document
from langchain_chroma import Chroma

from utils.embedding import embedding
from config import VECTOR_DB
from config import URL_FILE

db = Chroma(
    persist_directory=VECTOR_DB,
    embedding_function=embedding
)


def fetch(url):

    html = requests.get(url).text

    soup = BeautifulSoup(html, "html.parser")

    return soup.get_text()


def update_database():

    with open(URL_FILE, "r") as f:

        urls = f.readlines()

    for url in urls:

        try:

            text = fetch(url.strip())

            doc = Document(page_content=text)

            db.add_documents([doc])

        except Exception as e:

            print(e)

    print("Knowledge Base Updated")