import os
from groq import Groq
from config import GROQ_MODEL


def get_client():
    try:
        import streamlit as st
        api_key = st.secrets["GROQ_API_KEY"]
    except Exception:
        api_key = os.environ.get("GROQ_API_KEY", "")
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


def build_context(docs):
    context = ""
    for i, doc in enumerate(docs):
        content = getattr(doc, "page_content", str(doc))
        context += f"[Source {i+1}]: {content}\n"
    return context


def generate_streaming_response(query: str, docs):
    client = get_client()

    context = build_context(docs)

    # ✅ No data fallback
    if not context.strip():
        yield "I don't have enough information from the document."
        return

    messages = build_prompt(query, context)

    try:
        stream = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=messages,
            max_tokens=512,      # faster streaming
            temperature=0.2,
            stream=True          # 🔥 MUST for streaming
        )

        for chunk in stream:
            # ✅ safe handling
            if not chunk.choices:
                continue

            delta = chunk.choices[0].delta

            # ✅ only yield actual tokens
            if hasattr(delta, "content") and delta.content:
                yield delta.content

    except Exception as e:
        yield f"\n\n⚠️ Error: {str(e)}"
