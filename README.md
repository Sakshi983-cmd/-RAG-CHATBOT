<div align="center">

# 🧠 DocMind AI
### RAG Chatbot · Powered by Groq · Built for Amlgo Labs

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Groq](https://img.shields.io/badge/Groq-LLaMA_3.1-F55036?style=for-the-badge&logo=groq&logoColor=white)](https://groq.com)
[![FAISS](https://img.shields.io/badge/FAISS-Vector_DB-0467DF?style=for-the-badge&logo=meta&logoColor=white)](https://faiss.ai)
[![License](https://img.shields.io/badge/License-MIT-10b981?style=for-the-badge)](LICENSE)

> **An AI-powered chatbot that reads your documents and answers questions in real-time using Retrieval-Augmented Generation (RAG) with streaming responses.**

![DocMind AI Screenshot](assets/screenshots/app_screenshot.png)

[🚀 Live Demo](https://nhvb3mmj3ngfnosel4f9hf.streamlit.app) · [📂 Source Code](#-folder-structure) · [⚙️ Setup](#%EF%B8%8F-setup--installation)

</div>

---

## 🏗️ Architecture
```
┌─────────────────────────────────────────────────────────────────┐
│                        DocMind AI Pipeline                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│   📄 PDF / TXT                                                    │
│        │                                                          │
│        ▼                                                          │
│   ┌─────────────┐    clean +     ┌─────────────┐                 │
│   │  Document   │   chunk into   │   Chunks    │                 │
│   │  Processor  │ ─────────────► │  (200 words │                 │
│   └─────────────┘   100-300 w    │   + overlap)│                 │
│                                  └──────┬──────┘                 │
│                                         │ embed                  │
│                                         ▼                        │
│                                  ┌─────────────┐                 │
│                                  │ all-MiniLM  │                 │
│                                  │  Embeddings │                 │
│                                  └──────┬──────┘                 │
│                                         │ store                  │
│                                         ▼                        │
│   👤 User Query                  ┌─────────────┐                 │
│        │                         │  FAISS      │                 │
│        │ embed query             │  Vector DB  │                 │
│        ▼                         └──────┬──────┘                 │
│   ┌─────────────┐   top-4 chunks        │                        │
│   │  Retriever  │ ◄─────────────────────┘                        │
│   └──────┬──────┘                                                 │
│          │ context + query                                        │
│          ▼                                                        │
│   ┌─────────────┐   streaming    ┌─────────────┐                 │
│   │  Groq LLM   │ ─────────────► │  Streamlit  │                 │
│   │  LLaMA 3.1  │   token/token  │     UI      │                 │
│   └─────────────┘                └─────────────┘                 │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## ✨ Features

| Feature | Description |
|---|---|
| 📄 **Multi-format Upload** | Supports PDF and TXT documents |
| 🔍 **Semantic Search** | FAISS vector similarity search |
| ⚡ **Real-time Streaming** | Token-by-token response like ChatGPT |
| 📚 **Source Attribution** | Shows exactly which chunks were used |
| 🎨 **Beautiful Dark UI** | Custom CSS with Syne + Space Mono fonts |
| 🧹 **Smart Chunking** | Sentence-aware splitting with overlap |
| 🔒 **Secure API** | Keys stored in Streamlit secrets |
| 🗑️ **Clear Chat** | Reset conversation anytime |

---

## 🛠️ Tech Stack

| Layer | Technology | Why |
|---|---|---|
| LLM | llama-3.1-8b-instant | Fast, free, accurate |
| API | Groq Cloud | Zero local GPU needed |
| Embeddings | all-MiniLM-L6-v2 | ~90MB, CPU friendly |
| Vector DB | FAISS (CPU) | No server, lightweight |
| UI | Streamlit | Quick, beautiful |
| PDF Parse | pypdf | Reliable extraction |

---

## 📁 Folder Structure
```
rag-chatbot-amlgo/
│
├── 📂 data/                    ← Input documents (PDF/TXT)
├── 📂 chunks/                  ← Processed JSON chunks
├── 📂 vectordb/                ← FAISS index files
├── 📂 notebooks/               ← Exploration notebooks
├── 📂 assets/screenshots/      ← App screenshots
│
├── 📂 src/
│   ├── __init__.py
│   ├── document_processor.py   ← Clean + chunk documents
│   ├── embeddings.py           ← Generate + store embeddings
│   ├── retriever.py            ← Semantic search
│   └── generator.py            ← Groq LLM + streaming
│
├── 🐍 app.py                   ← Streamlit main app
├── ⚙️  config.py               ← All settings centralized
├── 📋 requirements.txt
└── 📖 README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/Sakshi983-cmd/-RAG-CHATBOT.git
cd -RAG-CHATBOT
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

### 4. Get Groq API Key (Free)
- Go to [console.groq.com](https://console.groq.com)
- Create a free account
- Copy your API key

### 5. Setup Streamlit secrets
Create `.streamlit/secrets.toml`:
```toml
GROQ_API_KEY = "gsk_your_key_here"
```

### 6. Run the app
```bash
streamlit run app.py
```

---

## 💬 Sample Queries & Responses

### ✅ Success Case 1
**Q: What is the refund policy?**

**A:** Refund requests must be submitted within 14 days. Payments are non-refundable except where service was not delivered. A 7-day free trial is available.

### ✅ Success Case 2
**Q: What data does TechVault collect?**

**A:** TechVault collects name, email address, payment information, IP address, and browsing behavior.

### ✅ Success Case 3
**Q: What activities are prohibited?**

**A:** Prohibited activities include unlawful use, unauthorized access, uploading malicious code, data scraping, impersonation, and spam.

### ❌ Failure Case
**Q: What is the CEO's name?**

**A:** I could not find this information in the provided document.

---

## 🧠 Design Decisions

**Why Groq instead of local LLM?**
Local models like Mistral-7B require 8GB+ GPU RAM. Groq runs the same models with zero local resource usage and 10x faster inference.

**Why all-MiniLM-L6-v2?**
At only ~90MB, it runs on CPU in under 2 seconds. Larger models offer marginal quality gains but 5x the memory cost.

**Why FAISS over Chroma/Qdrant?**
FAISS requires no server, stores as a simple file, and handles our document size with sub-millisecond search.

**Chunk size: 200 words with 30-word overlap**
Best balance — small enough for precise retrieval, large enough for coherent context.

---

## 📸 Demo

![App Screenshot](assets/app_screenshot.png)

🔗 **Live App:** https://nhvb3mmj3ngfnosel4f9hf.streamlit.app

---

<div align="center">
Built with ❤️ by Sakshi | Amlgo Labs Assignment 2025
</div>
