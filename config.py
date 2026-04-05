import os
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "llama-3.1-8b-instant"  
EMBEDDING_MODEL = "all-MiniLM-L6-v2"  

CHUNK_SIZE = 200     
CHUNK_OVERLAP = 30     

TOP_K_RESULTS = 4

DATA_DIR = "data"
CHUNKS_DIR = "chunks"
VECTORDB_DIR = "vectordb"
VECTORDB_PATH = f"{VECTORDB_DIR}/faiss_index"
CHUNKS_PATH = f"{CHUNKS_DIR}/chunks.json"
