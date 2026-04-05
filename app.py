import os
import streamlit as st

st.set_page_config(page_title="RAG Chatbot", page_icon="🤖", layout="wide")

# Session state
for key, val in {
    "messages": [], "vectordb_loaded": False,
    "index": None, "chunks": None, "num_chunks": 0
}.items():
    if key not in st.session_state:
        st.session_state[key] = val

# ── Sidebar ──────────────────────────────────────────────────
with st.sidebar:
    st.title("⚙️ Settings")
    st.markdown("---")

    st.markdown("### 🔑 Groq API Key")
    api_key = st.text_input("Enter Groq API Key", type="password", placeholder="gsk_...")
    if api_key:
        os.environ["GROQ_API_KEY"] = api_key
        st.success("✅ API Key set!")

    st.markdown("---")
    st.markdown("### 🤖 Model Info")
    st.info("**LLM:** llama-3.1-8b-instant")
    st.info("**Embeddings:** all-MiniLM-L6-v2")
    st.info("**Top-K:** 4 chunks")

    st.markdown("---")
    st.markdown("### 📄 Upload Document")
    uploaded_file = st.file_uploader("Upload PDF or TXT", type=["pdf", "txt"])

    if uploaded_file and st.button("🔄 Process Document", use_container_width=True):
        if not api_key:
            st.error("❌ Enter Groq API Key first!")
        else:
            with st.spinner("Processing... ⏳"):
                try:
                    from src.document_processor import process_document
                    from src.embeddings import create_and_save_vectordb

                    os.makedirs("data", exist_ok=True)
                    file_path = os.path.join("data", uploaded_file.name)
                    with open(file_path, "wb") as f:
                        f.write(uploaded_file.getbuffer())

                    chunks = process_document(file_path)
                    index, chunks = create_and_save_vectordb(chunks)

                    st.session_state.index = index
                    st.session_state.chunks = chunks
                    st.session_state.num_chunks = len(chunks)
                    st.session_state.vectordb_loaded = True
                    st.session_state.messages = []
                    st.success(f"✅ {len(chunks)} chunks created!")
                except Exception as e:
                    st.error(f"❌ {str(e)}")

    st.markdown("---")
    st.markdown("### 📊 Stats")
    if st.session_state.vectordb_loaded:
        st.success("✅ Vector DB Ready")
        st.metric("Total Chunks", st.session_state.num_chunks)
    else:
        st.warning("⚠️ No document loaded")

    st.markdown("---")
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# ── Main Chat ─────────────────────────────────────────────────
st.title("🤖 RAG Chatbot — Amlgo Labs")
st.markdown("Upload a document from sidebar, then ask questions!")
st.markdown("---")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message["role"] == "assistant" and "sources" in message:
            with st.expander("📚 Source Chunks"):
                for i, src in enumerate(message["sources"]):
                    st.markdown(f"**Source {i+1}** (Chunk ID: {src['chunk_id']})")
                    st.text(src["text"][:300] + "..." if len(src["text"]) > 300 else src["text"])
                    st.markdown("---")

if prompt := st.chat_input("Ask a question about your document..."):
    if not api_key:
        st.warning("⚠️ Enter Groq API Key in sidebar!")
        st.stop()
    if not st.session_state.vectordb_loaded:
        st.warning("⚠️ Upload and process a document first!")
        st.stop()

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        from src.retriever import retrieve_relevant_chunks, format_context
        from src.generator import generate_streaming_response

        retrieved = retrieve_relevant_chunks(prompt, st.session_state.index, st.session_state.chunks)
        context = format_context(retrieved)

        placeholder = st.empty()
        full_response = ""
        try:
            for token in generate_streaming_response(prompt, context):
                full_response += token
                placeholder.markdown(full_response + "▌")
            placeholder.markdown(full_response)
        except Exception as e:
            full_response = f"❌ Error: {str(e)}"
            placeholder.markdown(full_response)

        with st.expander("📚 Source Chunks Used"):
            for i, src in enumerate(retrieved):
                st.markdown(f"**Source {i+1}** (Chunk ID: {src['chunk_id']})")
                st.text(src["text"][:300] + "..." if len(src["text"]) > 300 else src["text"])
                st.markdown("---")

    st.session_state.messages.append({
        "role": "assistant",
        "content": full_response,
        "sources": retrieved
    })
