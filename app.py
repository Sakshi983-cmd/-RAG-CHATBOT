import os
import streamlit as st
from config import GROQ_MODEL, EMBEDDING_MODEL, TOP_K_RESULTS, VECTORDB_PATH, CHUNKS_PATH
from src.document_processor import process_document
from src.embeddings import create_and_save_vectordb, load_vectordb
from src.retriever import retrieve_relevant_chunks, format_context
from src.generator import generate_streaming_response

# ─── Page Config ────────────────────────────────────────────
st.set_page_config(
    page_title="RAG Chatbot",
    page_icon="🤖",
    layout="wide"
)

# ─── Session State Initialize ───────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

if "vectordb_loaded" not in st.session_state:
    st.session_state.vectordb_loaded = False

if "index" not in st.session_state:
    st.session_state.index = None

if "chunks" not in st.session_state:
    st.session_state.chunks = None

if "num_chunks" not in st.session_state:
    st.session_state.num_chunks = 0


# ─── Load existing vectordb if available ────────────────────
def try_load_existing_vectordb():
    """Agar pehle se vectordb saved hai toh load karo."""
    if os.path.exists(f"{VECTORDB_PATH}.index") and os.path.exists(f"{VECTORDB_PATH}.pkl"):
        try:
            index, chunks = load_vectordb()
            st.session_state.index = index
            st.session_state.chunks = chunks
            st.session_state.num_chunks = len(chunks)
            st.session_state.vectordb_loaded = True
            return True
        except Exception:
            return False
    return False


# Auto load on startup
if not st.session_state.vectordb_loaded:
    try_load_existing_vectordb()


# ─── Sidebar ────────────────────────────────────────────────
with st.sidebar:
    st.title("⚙️ Settings")
    st.markdown("---")

    # Model info
    st.markdown("### 🤖 Model Info")
    st.info(f"**LLM:** {GROQ_MODEL}")
    st.info(f"**Embeddings:** {EMBEDDING_MODEL}")
    st.info(f"**Top-K Retrieval:** {TOP_K_RESULTS}")

    st.markdown("---")

    # Document upload
    st.markdown("### 📄 Upload Document")
    uploaded_file = st.file_uploader(
        "Upload PDF or TXT file",
        type=["pdf", "txt"],
        help="Upload the document you want to chat with"
    )

    if uploaded_file is not None:
        if st.button("🔄 Process Document", use_container_width=True):
            with st.spinner("Processing document..."):
                try:
                    # File save karo data/ folder mein
                    os.makedirs("data", exist_ok=True)
                    file_path = os.path.join("data", uploaded_file.name)
                    with open(file_path, "wb") as f:
                        f.write(uploaded_file.getbuffer())

                    # Process karo
                    chunks = process_document(file_path)

                    # Embeddings aur vectordb banao
                    index, chunks = create_and_save_vectordb(chunks)

                    # Session state update karo
                    st.session_state.index = index
                    st.session_state.chunks = chunks
                    st.session_state.num_chunks = len(chunks)
                    st.session_state.vectordb_loaded = True
                    st.session_state.messages = []  # Clear chat

                    st.success(f"✅ Document processed! {len(chunks)} chunks created.")
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")

    st.markdown("---")

    # DB Stats
    st.markdown("### 📊 Database Stats")
    if st.session_state.vectordb_loaded:
        st.success(f"✅ Vector DB Ready")
        st.metric("Total Chunks", st.session_state.num_chunks)
    else:
        st.warning("⚠️ No document loaded")

    st.markdown("---")

    # Clear chat button
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


# ─── Main Chat Interface ─────────────────────────────────────
st.title("🤖 RAG Chatbot")
st.markdown("Ask questions about your uploaded document!")
st.markdown("---")

# Chat history dikhao
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        # Source chunks dikhao agar assistant message hai
        if message["role"] == "assistant" and "sources" in message:
            with st.expander("📚 View Source Chunks"):
                for i, source in enumerate(message["sources"]):
                    st.markdown(f"**Source {i+1}** (Chunk ID: {source['chunk_id']})")
                    st.text(source["text"][:300] + "..." if len(source["text"]) > 300 else source["text"])
                    st.markdown("---")

# User input
if prompt := st.chat_input("Ask a question about your document..."):

    # Check karo document loaded hai ya nahi
    if not st.session_state.vectordb_loaded:
        st.warning("⚠️ Please upload and process a document first!")
        st.stop()

    # User message add karo
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Assistant response
    with st.chat_message("assistant"):
        # Relevant chunks retrieve karo
        retrieved_chunks = retrieve_relevant_chunks(
            prompt,
            st.session_state.index,
            st.session_state.chunks
        )

        # Context banao
        context = format_context(retrieved_chunks)

        # Streaming response
        response_placeholder = st.empty()
        full_response = ""

        try:
            for token in generate_streaming_response(prompt, context):
                full_response += token
                response_placeholder.markdown(full_response + "▌")  # Cursor effect

            response_placeholder.markdown(full_response)  # Final response

        except Exception as e:
            full_response = f"❌ Error generating response: {str(e)}"
            response_placeholder.markdown(full_response)

        # Source chunks dikhao
        with st.expander("📚 View Source Chunks Used"):
            for i, source in enumerate(retrieved_chunks):
                st.markdown(f"**Source {i+1}** (Chunk ID: {source['chunk_id']})")
                st.text(source["text"][:300] + "..." if len(source["text"]) > 300 else source["text"])
                st.markdown("---")

    # Assistant message history mein save karo
    st.session_state.messages.append({
        "role": "assistant",
        "content": full_response,
        "sources": retrieved_chunks
    })
