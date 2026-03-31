# 🤖 RAG Chatbot — Amlgo Labs Assignment

An AI-powered chatbot that answers questions from uploaded documents using a **Retrieval-Augmented Generation (RAG)** pipeline with real-time streaming responses.

---

## 🏗️ Architecture

```
User Query
    ↓
[Streamlit UI] → [Retriever] → FAISS Vector DB
                      ↓
               Top-K Relevant Chunks
                      ↓
              [Generator - Groq LLM]
                      ↓
           Streaming Response → [Streamlit UI]
```

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| LLM | `llama-3.1-8b-instant` via Groq API |
| Embeddings | `all-MiniLM-L6-v2` (SentenceTransformers) |
| Vector DB | FAISS (CPU) |
| UI | Streamlit |
| Streaming | Groq native streaming |

---

## 📁 Folder Structure

```
rag-chatbot-amlgo/
├── data/                    # Input documents
├── chunks/                  # Processed text chunks
├── vectordb/                # FAISS index files
├── notebooks/               # Exploration notebooks
├── assets/screenshots/      # App screenshots
├── src/
│   ├── document_processor.py   # Cleaning + chunking
│   ├── embeddings.py           # Embedding generation
│   ├── retriever.py            # Semantic search
│   └── generator.py            # Groq LLM + streaming
├── app.py                   # Streamlit app
├── config.py                # All settings
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/rag-chatbot-amlgo.git
cd rag-chatbot-amlgo
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup environment variables
```bash
cp .env.example .env
# .env file mein apni Groq API key daalo
```

Get your free Groq API key at: https://console.groq.com

### 5. Run the app
```bash
streamlit run app.py
```

---

## 💬 Sample Queries

- *"What are the main terms and conditions?"*
- *"What is the privacy policy regarding data sharing?"*
- *"What are the user's rights mentioned in this document?"*

---

## 📸 Demo

> Screenshots in `assets/screenshots/` folder

---

## 🧠 Model & Design Choices

- **Groq API** chosen for zero local GPU requirement and fast inference
- **all-MiniLM-L6-v2** chosen for lightweight CPU-friendly embeddings (~90MB)
- **FAISS** chosen over Chroma/Qdrant for simplicity and no server requirement
- **Chunk size 200 words** with 30-word overlap for context continuity
