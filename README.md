# Dynamic Knowledge Base Chatbot

## Overview

The **Dynamic Knowledge Base Chatbot** is a Retrieval-Augmented Generation (RAG) chatbot that automatically expands its knowledge base by periodically updating a vector database with information from local files and external web sources. The chatbot retrieves relevant context from the vector database and generates accurate responses using Google's Gemini AI.

This project demonstrates how a chatbot can continuously improve its knowledge without requiring manual retraining.

---

## Features

* Dynamic knowledge base expansion
* Automatic retrieval of information from local files and websites
* Vector database storage using ChromaDB
* Semantic search using HuggingFace Embeddings
* Google Gemini integration for response generation
* Scheduled database updates
* Simple Streamlit-based user interface
* Modular and easy-to-maintain project structure

---

## Tech Stack

* Python
* Streamlit
* LangChain
* ChromaDB
* HuggingFace Sentence Transformers
* Google Gemini API
* BeautifulSoup
* Requests
* Schedule

---

## Project Structure

```text
Dynamic-Knowledge-Chatbot/
│
├── app.py
├── create_db.py
├── update_db.py
├── scheduler.py
├── config.py
├── requirements.txt
├── README.md
│
├── knowledge/
│   ├── data.txt
│   └── urls.txt
│
├── utils/
│   ├── embedding.py
│   ├── loader.py
│   ├── retriever.py
│   └── vectordb.py
│
└── vector_db/
```

---

## How It Works

1. Load knowledge from local text files.
2. Convert documents into vector embeddings.
3. Store embeddings in ChromaDB.
4. Periodically fetch new information from websites.
5. Add newly fetched content to the vector database.
6. Retrieve the most relevant documents for user queries.
7. Generate accurate responses using Google Gemini.

---

## Workflow

```text
Local Files / Websites
          │
          ▼
Document Loader
          │
          ▼
Text Embeddings
          │
          ▼
Chroma Vector Database
          │
          ▼
Retriever
          │
          ▼
Google Gemini
          │
          ▼
Chatbot Response
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Dynamic-Knowledge-Chatbot.git
cd Dynamic-Knowledge-Chatbot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Create the initial vector database:

```bash
python create_db.py
```

Run the scheduler to update the knowledge base automatically:

```bash
python scheduler.py
```

Launch the chatbot:

```bash
streamlit run app.py
```

---

## Future Enhancements

* PDF document ingestion
* Support for multiple document formats
* Duplicate document detection
* Incremental vector database updates
* Real-time web crawling
* Multi-language support
* Authentication and user management
* Conversation memory

---

## Learning Outcomes

* Retrieval-Augmented Generation (RAG)
* Vector databases
* Semantic search
* Embedding models
* LangChain pipelines
* Google Gemini API integration
* Automated knowledge base updates
* Streamlit application development

---

## Author

**Yash Rawal**

B.Tech – Computer Science Engineering (AI & ML)

JECRC University

GitHub: https://github.com/Yashrawal03
