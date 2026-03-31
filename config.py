import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ─── Groq API ───────────────────────────────────────────────
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "llama-3.1-8b-instant"  # Fast + free on Groq

# ─── Embedding Model ────────────────────────────────────────
EMBEDDING_MODEL = "all-MiniLM-L6-v2"  # Lightweight, ~90MB, CPU friendly

# ─── Document Chunking ──────────────────────────────────────
CHUNK_SIZE = 200        # words per chunk (100-300 as per assignment)
CHUNK_OVERLAP = 30      # overlap between chunks for context continuity

# ─── Retriever ──────────────────────────────────────────────
TOP_K_RESULTS = 4       # how many chunks to retrieve per query

# ─── Paths ──────────────────────────────────────────────────
DATA_DIR = "data"
CHUNKS_DIR = "chunks"
VECTORDB_DIR = "vectordb"
VECTORDB_PATH = f"{VECTORDB_DIR}/faiss_index"
CHUNKS_PATH = f"{CHUNKS_DIR}/chunks.json"
