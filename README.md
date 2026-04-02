<div align="center">

<!-- Animated Header -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=180&section=header&text=Hi%20there!%20I'm%20Sakshi%20%F0%9F%91%8B&fontSize=42&fontColor=fff&animation=twinkling&fontAlignY=32&desc=Junior%20AI%20Engineer%20%7C%20RAG%20%7C%20LLMs%20%7C%20Streamlit&descAlignY=55&descSize=18"/>

<!-- Typing Animation -->
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=7C3AED&center=true&vCenter=true&width=600&lines=Building+AI-powered+applications+%F0%9F%A4%96;RAG+Chatbots+%7C+LLMs+%7C+Vector+DBs;Groq+%7C+FAISS+%7C+Streamlit+%7C+Python;Open+to+AI+Engineer+opportunities+%F0%9F%9A%80" alt="Typing SVG" />

<br/>

<!-- Profile Views + Followers -->
![Profile Views](https://komarev.com/ghpvc/?username=Sakshi983-cmd&color=7c3aed&style=for-the-badge&label=PROFILE+VIEWS)
[![GitHub followers](https://img.shields.io/github/followers/Sakshi983-cmd?style=for-the-badge&color=06b6d4&labelColor=0a0a0f&label=FOLLOWERS)](https://github.com/Sakshi983-cmd)

</div>

---

<!-- About Me -->
<img align="right" width="300" src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDd2dHZjbzRtNnVyZjFkdzFzMXFrbnR6Mm8ydGZxdzVldGZhMGowNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/qgQUggAC3Pfv687qPC/giphy.gif"/>

### 🧠 About Me

```python
class SakshiAIEngineer:
    name       = "Sakshi"
    role       = "Junior AI Engineer"
    location   = "India 🇮🇳"
    
    skills     = ["RAG Pipelines", "LLMs", 
                  "Vector DBs", "Streamlit"]
    
    current    = "DocMind AI — RAG Chatbot"
    llm        = "llama-3.1-8b via Groq"
    vector_db  = "FAISS"
    embeddings = "all-MiniLM-L6-v2"
    
    def say_hi(self):
        return "Let's build something with AI! 🚀"
```

<br clear="right"/>

---
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text=DocMind%20AI%20%F0%9F%A7%A0&fontSize=55&fontColor=fff&animation=twinkling&fontAlignY=36&desc=RAG%20Chatbot%20%7C%20Groq%20%7C%20FAISS%20%7C%20Streamlit&descAlignY=58&descSize=18"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=1000&color=7C3AED&center=true&vCenter=true&width=700&lines=Upload+any+document.+Ask+anything.+%F0%9F%93%84;Retrieval-Augmented+Generation+Pipeline+%F0%9F%94%8D;Real-time+Streaming+Responses+%E2%9A%A1;Powered+by+Groq+%2B+FAISS+%2B+all-MiniLM+%F0%9F%A4%96;Built+for+Amlgo+Labs+Junior+AI+Engineer+Role+%F0%9F%9A%80" alt="Typing SVG" />

<br/>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Groq](https://img.shields.io/badge/Groq-LLaMA_3.1-F55036?style=for-the-badge)](https://groq.com)
[![FAISS](https://img.shields.io/badge/FAISS-Vector_DB-0467DF?style=for-the-badge&logo=meta&logoColor=white)](https://faiss.ai)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-all--MiniLM-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co)
[![License](https://img.shields.io/badge/License-MIT-10b981?style=for-the-badge)](LICENSE)

<br/>

### 🔴 [LIVE APP → nhvb3mmj3ngfnosel4f9hf.streamlit.app](https://nhvb3mmj3ngfnosel4f9hf.streamlit.app)

</div>

---

## 📸 App Preview

<div align="center">

![DocMind AI](assets/app_screenshot.png)

</div>

---



## 🏗️ Architecture

## 🏗️ System Architecture (RAG Pipeline)

```mermaid
graph LR

A["📄 User Upload (PDF/TXT)"] --> B["🧹 Document Processor<br/>Clean + Chunk"]
B --> C["🔢 Embeddings<br/>MiniLM (384-dim)"]
C --> D["🗃️ FAISS Vector DB"]

E["👤 User Query"] --> F["🔍 Retriever<br/>Top-K Search"]
D --> F

F --> G["🧠 Generator<br/>Prompt Builder"]
G --> H["⚡ Groq API<br/>LLaMA 3"]
H --> I["🎨 Streamlit UI<br/>Response"]

style A fill:#e3f2fd
style I fill:#c8e6c9
style H fill:#fff3e0
style D fill:#f3e5f5

## ✨ Features

| | Feature | Details |
|:---:|---|---|
| 📄 | **Multi-format Upload** | PDF and TXT documents supported |
| ✂️ | **Smart Chunking** | Sentence-aware 200-word splits with 30-word overlap |
| 🔢 | **Dense Embeddings** | all-MiniLM-L6-v2 → 384-dim vectors |
| 🗃️ | **Vector Search** | FAISS IndexFlatL2, Top-K=4 retrieval |
| ⚡ | **Real-time Streaming** | Token-by-token like ChatGPT using Groq |
| 📚 | **Source Attribution** | Shows exact chunks used per answer |
| 🎨 | **Premium Dark UI** | Syne + Space Mono fonts, custom CSS |
| 🔒 | **Secure** | API key in Streamlit secrets, never in code |
| 🧠 | **Grounded Answers** | LLM refuses to hallucinate beyond context |
| 🗑️ | **Clear Chat** | Full session reset anytime |

---

## 🛠️ Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-F55036?style=for-the-badge&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![FAISS](https://img.shields.io/badge/FAISS-0467DF?style=for-the-badge&logo=meta&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

</div>

| Layer | Technology | Why Chosen |
|---|---|---|
| 🤖 **LLM** | `llama-3.1-8b-instant` via Groq | Zero GPU, ~300ms latency, free tier |
| 🔢 **Embeddings** | `all-MiniLM-L6-v2` | 90MB only, CPU-friendly, great semantic quality |
| 🗃️ **Vector DB** | `FAISS IndexFlatL2` | No server, file-based, sub-ms search |
| 🖥️ **UI** | `Streamlit` | Native streaming support, rapid development |
| 📄 **PDF** | `pypdf` | Reliable multi-page text extraction |
| ⚙️ **Config** | `python-dotenv` | Clean separation of secrets and code |

---



## 📁 Project Structure

```
📦 RAG-CHATBOT/
│
├── 📂 data/                         ← Upload documents here
│   └── 📄 your_document.pdf
│
├── 📂 chunks/                       ← Auto-generated JSON chunks
│   └── 📄 chunks.json
│
├── 📂 vectordb/                     ← Auto-generated FAISS index
│   ├── 🗃️ faiss_index.index
│   └── 🗃️ faiss_index.pkl
│
├── 📂 notebooks/                    ← Exploration & experiments
│
├── 📂 assets/
│   └── 📂 screenshots/
│       └── 🖼️ app_screenshot.png
│
├── 📂 src/
│   ├── 🐍 __init__.py
│   ├── 🐍 document_processor.py    ← load → clean → chunk → save
│   ├── 🐍 embeddings.py            ← embed → FAISS index → save/load
│   ├── 🐍 retriever.py             ← query embed → FAISS search → chunks
│   └── 🐍 generator.py             ← prompt build → Groq stream → yield tokens
│
├── 🐍 app.py                        ← Streamlit UI (main entry)
├── ⚙️  config.py                    ← All settings centralized
├── 📋 requirements.txt
├── 🔒 .env.example
├── 🚫 .gitignore
└── 📖 README.md
```

---

## ⚙️ Setup & Run Locally

### 1. Clone
```bash
git clone https://github.com/Sakshi983-cmd/-RAG-CHATBOT.git
cd -RAG-CHATBOT
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Get free Groq API key
👉 [console.groq.com](https://console.groq.com) → Sign up → Copy key

### 5. Add Streamlit secrets
Create `.streamlit/secrets.toml`:
```toml
GROQ_API_KEY = "gsk_xxxxxxxxxxxxxxxxxxxx"
```

### 6. Run!
```bash
streamlit run app.py
```

---

## 💬 Sample Queries & Responses

### ✅ Success — Refund Policy
```
Q: What is the refund policy?

A: According to the document, the refund policy is:
   • Refund requests must be submitted within 14 days of the charge
   • Payments are non-refundable except where TechVault failed to deliver
   • A 7-day free trial is available, auto-charged unless cancelled
```

### ✅ Success — Data Collection
```
Q: What data does TechVault collect?

A: TechVault Inc. collects personal data including name, email address,
   payment information, IP address, and browsing behavior within the platform.
```

### ✅ Success — Prohibited Activities
```
Q: What activities are prohibited?

A: Prohibited activities include unlawful use, unauthorized access,
   uploading malicious code, data scraping without consent,
   impersonation, harassment, and sending spam.
```

### ❌ Failure — Out of Scope (Hallucination Prevention)
```
Q: What is the CEO's name?

A: I could not find this information in the provided document.
```
> ✅ Model correctly refuses to hallucinate — stays grounded in document only.

---

## 🧠 Design Decisions

**Why Groq over local Mistral/LLaMA?**
Local models like Mistral-7B require 8GB+ VRAM. Groq runs the same llama-3.1-8b model on cloud infrastructure with ~300ms response time and zero local resource usage — ideal for laptop deployment.

**Why all-MiniLM-L6-v2?**
At 90MB with 384-dim output, it runs on CPU in under 2 seconds per batch. Larger models like bge-large-en offer 2-3% quality gain at 5x memory cost — not worth it for this use case.

**Why FAISS over Chroma or Qdrant?**
FAISS requires no server process, persists as two simple files (`.index` + `.pkl`), and handles sub-1000 chunk collections with sub-millisecond search. Chroma and Qdrant add operational overhead not justified here.

**Why 200-word chunks with 30-word overlap?**
Tested 100/200/300 word sizes. 100 words was too sparse for coherent answers. 300 words reduced retrieval precision. 200 words with 30-word overlap gave the best balance of precision and context richness.

**Why temperature=0.2?**
Lower temperature reduces creativity and increases factual consistency — critical for a document Q&A system where hallucination must be minimized.

---

## 📊 Evaluation

| Criteria | Weight | Implementation |
|---|---|---|
| ✅ Functionality & Integration | 30% | Full RAG pipeline working end-to-end |
| ✅ Streaming Output | 20% | Groq native stream, token-by-token |
| ✅ Code Quality | 20% | Modular src/, config.py, clean separation |
| ✅ Grounded Answers | 20% | Strict system prompt, refuses hallucination |
| ✅ App Usability & UX | 10% | Dark theme, source chunks, status indicators |

---

## ⚠️ Known Limitations

- Large documents (50+ pages) may take 30-60 seconds to process on first upload
- Groq free tier has rate limits — heavy usage may hit limits
- Image-based PDFs (scanned) are not supported — text extraction only
- Model may occasionally miss answers if relevant info spans multiple chunks

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=120&section=footer&text=Built%20for%20Amlgo%20Labs%20%F0%9F%9A%80&fontSize=24&fontColor=fff&fontAlignY=65"/>

**Made with ❤️ by Sakshi | Amlgo Labs Junior AI Engineer Assignment 2025**

⭐ Star this repo if you found it useful!

</div>
<!-- Featured Project -->
## 🚀 Featured Project — DocMind AI
