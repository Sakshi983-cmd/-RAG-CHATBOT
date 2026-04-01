import os
import json
import re
from pypdf import PdfReader
from config import CHUNK_SIZE, CHUNK_OVERLAP, CHUNKS_PATH


def load_document(file_path: str) -> str:
    ext = os.path.splitext(file_path)[-1].lower()
    if ext == ".pdf":
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
    elif ext == ".txt":
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        raise ValueError(f"Unsupported file type: {ext}")
    return text


def clean_text(text: str) -> str:
    text = re.sub(r" +", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"Page\s+\d+\s+of\s+\d+", "", text, flags=re.IGNORECASE)
    return text.strip()


def split_into_chunks(text: str, chunk_size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> list:
    sentences = re.split(r"(?<=[.!?])\s+", text)
    chunks = []
    current_words = []
    current_count = 0
    chunk_id = 0

    for sentence in sentences:
        words = sentence.split()
        word_count = len(words)

        if current_count + word_count > chunk_size and current_words:
            chunks.append({
                "chunk_id": chunk_id,
                "text": " ".join(current_words),
                "word_count": current_count
            })
            chunk_id += 1
            current_words = current_words[-overlap:] + words
            current_count = len(current_words)
        else:
            current_words.extend(words)
            current_count += word_count

    if current_words:
        chunks.append({
            "chunk_id": chunk_id,
            "text": " ".join(current_words),
            "word_count": current_count
        })
    return chunks


def save_chunks(chunks: list, path: str = CHUNKS_PATH) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2, ensure_ascii=False)


def load_chunks(path: str = CHUNKS_PATH) -> list:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def process_document(file_path: str) -> list:
    raw_text = load_document(file_path)
    clean = clean_text(raw_text)
    chunks = split_into_chunks(clean)
    save_chunks(chunks)
    return chunks
