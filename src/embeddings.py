import os
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from config import EMBEDDING_MODEL, VECTORDB_PATH

_model = None

def get_embedding_model():
    global _model
    if _model is None:
        _model = SentenceTransformer(EMBEDDING_MODEL)
    return _model


def generate_embeddings(chunks: list) -> np.ndarray:
    model = get_embedding_model()
    texts = [chunk["text"] for chunk in chunks]
    return model.encode(texts, show_progress_bar=True, convert_to_numpy=True)


def build_faiss_index(embeddings: np.ndarray):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings.astype(np.float32))
    return index


def save_vectordb(index, chunks: list, path: str = VECTORDB_PATH) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    faiss.write_index(index, f"{path}.index")
    with open(f"{path}.pkl", "wb") as f:
        pickle.dump(chunks, f)


def load_vectordb(path: str = VECTORDB_PATH):
    index = faiss.read_index(f"{path}.index")
    with open(f"{path}.pkl", "rb") as f:
        chunks = pickle.load(f)
    return index, chunks


def create_and_save_vectordb(chunks: list):
    embeddings = generate_embeddings(chunks)
    index = build_faiss_index(embeddings)
    save_vectordb(index, chunks)
    return index, chunks
