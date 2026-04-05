import numpy as np
from config import TOP_K_RESULTS
from src.embeddings import get_embedding_model


def retrieve_relevant_chunks(query: str, index, chunks: list, top_k: int = TOP_K_RESULTS) -> list:
    model = get_embedding_model()
    query_embedding = model.encode([query], convert_to_numpy=True).astype(np.float32)
    distances, indices = index.search(query_embedding, top_k)
    results = []
    for i, idx in enumerate(indices[0]):
        if idx != -1:
            chunk = chunks[idx].copy()
            chunk["relevance_score"] = float(distances[0][i])
            results.append(chunk)
    return results


def format_context(retrieved_chunks: list) -> str:
    parts = []
    for i, chunk in enumerate(retrieved_chunks):
        # 150 words per chunk = safe token usage even with 4 chunks
        words = chunk['text'].split()[:150]
        parts.append(f"[Source {i+1}]\n{' '.join(words)}")
    return "\n\n".join(parts)
