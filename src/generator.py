import os
from groq import Groq
from config import GROQ_MODEL


def get_client():
    import streamlit as st

    api_key = st.secrets.get("GROQ_API_KEY")

    if not api_key:
        raise ValueError("❌ API key missing")

    return Groq(api_key=api_key)


def build_prompt(query: str, context: str) -> list:
    system_message = """You are an AI assistant specialized in answering questions from documents.

STRICT RULES:
1. Answer ONLY using the provided context.
2. If the answer is not found, say: "I don't have enough information from the document."
3. ALWAYS include sources in the format [Source 1], [Source 2].
4. Do NOT make up any information.
5. Be concise and accurate.

Output Format:
Answer: <your answer>

Sources:
[Source 1], [Source 2]
"""

    user_message = f"""Context from document:
{context}

User Question: {query}

Follow the output format strictly."""

    return [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message}
    ]


# 🔥 OPTIMIZED CONTEXT (token-safe)
def build_context(docs, max_chars=1000):
    context = ""

    for i, doc in enumerate(docs):
        content = getattr(doc, "page_content", str(doc))

        # limit each chunk
        content = content[:200]

        context += f"[Source {i+1}]: {content}\n"

    return context[:max_chars]


def generate_streaming_response(query: str, docs):
    client = get_client()

    context = build_context(docs)

    # safety guard
    if len(context) > 1000:
        context = context[:1000]

    # no data fallback
    if not context.strip():
        yield "I don't have enough information from the document."
        return

    messages = build_prompt(query, context)

    try:
        stream = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=messages,
            max_tokens=200,      # 🔥 safe limit
            temperature=0.2,
            stream=True
        )

        for chunk in stream:
            if not chunk.choices:
                continue

            delta = chunk.choices[0].delta

            if hasattr(delta, "content") and delta.content:
                yield delta.content

    except Exception as e:
        yield f"\n\n⚠️ Error: {str(e)}"
