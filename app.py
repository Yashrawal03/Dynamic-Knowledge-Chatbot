import streamlit as st
import google.generativeai as genai

from config import GOOGLE_API_KEY
from utils.retriever import retrieve

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("Dynamic Knowledge Chatbot")

question = st.text_input("Ask anything")

if question:

    docs = retrieve(question)

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
Use the context below to answer the question.

Context:
{context}

Question:
{question}
"""

    response = model.generate_content(prompt)

    st.write(response.text)