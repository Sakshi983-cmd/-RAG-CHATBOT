import os
from groq import Groq
from config import GROQ_MODEL


def get_client():
    # Pehle Streamlit secrets check karo, phir env variable
    try:
        import streamlit as st
        api_key = st.secrets["GROQ_API_KEY"]
    except Exception:
        api_key = os.environ.get("GROQ_API_KEY", "")
    return Groq(api_key=api_key)


def build_prompt(query: str, context: str) -> list:
    system_message = """You are a helpful AI assistant that answers questions strictly based on the provided document context.
Rules:
- Only answer using the information from the context below
- If the answer is not in the context, say "I could not find this information in the provided document"
- Be concise and accurate
- Do not make up information"""

    user_message = f"""Context from document:
{context}

User Question: {query}

Please answer based only on the context above."""

    return [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message}
    ]


def generate_streaming_response(query: str, context: str):
    """Token by token streaming for Streamlit."""
    client = get_client()
    messages = build_prompt(query, context)
    stream = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=messages,
        max_tokens=1024,
        temperature=0.2,
        stream=True
    )
    for chunk in stream:
        token = chunk.choices[0].delta.content
        if token is not None:
            yield token
