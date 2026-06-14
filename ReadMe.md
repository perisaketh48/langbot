# 🤖 LangBot

LangBot is a Retrieval-Augmented Generation (RAG) chatbot built using LangChain, FAISS, Gemini, and Streamlit.

The application retrieves relevant information from LangChain documentation and generates grounded responses using Gemini. Every answer is generated from retrieved documentation chunks and includes the source documents used.

---

## 🚀 Features

- RAG (Retrieval-Augmented Generation)
- FAISS Vector Database
- Ollama Embeddings (`mxbai-embed-large`)
- Gemini 2.5 Flash
- Dynamic Topic Discovery
- Source Attribution
- Streamlit UI
- Docker Support

---

## 🏗️ Architecture

```text
User Query
     │
     ▼
FAISS Retriever
     │
     ▼
Relevant Documentation Chunks
     │
     ▼
Gemini 2.5 Flash
     │
     ▼
Grounded Answer + Sources
```

---

## 📂 Project Structure

```text
LangBot
│
├── app.py
├── Dockerfile
├── requirements.txt
├── README.md
│
├── data
│   ├── langchain_document.json
│   └── langchain_rag_docs.json
│
├── faiss_index
│   ├── index.faiss
│   └── index.pkl
│
└── scripts
    ├── data_collection.py
    ├── data_filtering.py
    └── data_ingestion.py
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone <repository-url>
cd LangBot
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

Application will be available at:

```text
http://localhost:8501
```

---

## 🐳 Docker

### Build Image

```bash
docker build -t langbot .
```

### Run Container

```bash
docker run -p 8501:8501 --env-file .env langbot
```

Open:

```text
http://localhost:8501
```

---

## 📚 Knowledge Base

The chatbot is trained on selected LangChain documentation including:

- LangSmith
- Embeddings
- Document Loaders
- Retrieval
- Prompt Templates
- RAG Evaluation
- Observability
- Runnable Components

New documentation can be added by:

1. Updating the JSON data source.
2. Running the ingestion script.
3. Rebuilding the FAISS index.

---

## 🧠 Tech Stack

- Python
- LangChain
- FAISS
- Streamlit
- Gemini 2.5 Flash
- Ollama Embeddings
- Docker

---

## 📄 Example Questions

- What are embeddings?
- What is RAG?
- How does retrieval work?
- What is a document loader?
- Explain prompt templates.
- What is LangSmith?

---

## 🔍 Source Attribution

Every generated answer includes the documentation sources used during retrieval, allowing users to verify information directly from the original documentation.

---

## 🚀 Deployment

The application can be deployed using:

- Render
- Railway
- Azure Container Apps
- AWS ECS / Fargate
- Google Cloud Run

Environment variables must be configured on the deployment platform.

---

## 👨‍💻 Author

Saketh

Built using LangChain, FAISS, Gemini, Streamlit, and Docker.
