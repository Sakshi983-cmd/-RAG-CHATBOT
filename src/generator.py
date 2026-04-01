import os
import streamlit as st

st.set_page_config(
    page_title="DocMind AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── Custom CSS ──────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Syne', sans-serif;
    background-color: #0a0a0f;
    color: #e8e8f0;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem; max-width: 100%; }
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: #0a0a0f; }
::-webkit-scrollbar-thumb { background: #7c3aed; border-radius: 2px; }
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f0f1a 0%, #0a0a0f 100%);
    border-right: 1px solid #1e1e2e;
}
section[data-testid="stSidebar"] .block-container { padding: 1.5rem 1rem; }
.logo-area {
    text-align: center;
    padding: 1rem 0 1.5rem 0;
    border-bottom: 1px solid #1e1e2e;
    margin-bottom: 1.5rem;
}
.logo-title {
    font-family: 'Syne', sans-serif;
    font-weight: 800;
    font-size: 1.6rem;
    background: linear-gradient(135deg, #7c3aed, #06b6d4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: -0.5px;
}
.logo-sub {
    font-family: 'Space Mono', monospace;
    font-size: 0.65rem;
    color: #4a4a6a;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-top: 2px;
}
.sidebar-label {
    font-family: 'Space Mono', monospace;
    font-size: 0.65rem;
    color: #4a4a6a;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
    margin-top: 1rem;
}
.badge-row { display: flex; flex-direction: column; gap: 6px; margin-bottom: 1rem; }
.badge {
    display: flex; align-items: center; gap: 8px;
    background: #13131f; border: 1px solid #1e1e2e;
    border-radius: 8px; padding: 8px 12px;
    font-size: 0.78rem; color: #a0a0c0;
}
.badge-dot { width: 6px; height: 6px; border-radius: 50%; background: #7c3aed; flex-shrink: 0; }
.badge-dot.cyan { background: #06b6d4; }
.badge-dot.green { background: #10b981; }
.status-ready {
    display: inline-flex; align-items: center; gap: 6px;
    background: rgba(16,185,129,0.1); border: 1px solid rgba(16,185,129,0.3);
    border-radius: 20px; padding: 4px 12px;
    font-size: 0.75rem; color: #10b981; font-family: 'Space Mono', monospace;
}
.status-waiting {
    display: inline-flex; align-items: center; gap: 6px;
    background: rgba(245,158,11,0.1); border: 1px solid rgba(245,158,11,0.3);
    border-radius: 20px; padding: 4px 12px;
    font-size: 0.75rem; color: #f59e0b; font-family: 'Space Mono', monospace;
}
[data-testid="stFileUploader"] {
    background: #13131f; border: 1px dashed #2a2a3e;
    border-radius: 12px; padding: 0.5rem; transition: border-color 0.2s;
}
[data-testid="stFileUploader"]:hover { border-color: #7c3aed; }
.stButton > button {
    background: linear-gradient(135deg, #7c3aed, #5b21b6) !important;
    color: white !important; border: none !important;
    border-radius: 10px !important; font-family: 'Syne', sans-serif !important;
    font-weight: 600 !important; font-size: 0.85rem !important;
    padding: 0.6rem 1rem !important; transition: all 0.2s ease !important;
}
.stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 8px 20px rgba(124,58,237,0.4) !important;
}
.main-header { padding: 2rem 0 1.5rem 0; border-bottom: 1px solid #1e1e2e; margin-bottom: 2rem; }
.main-title {
    font-family: 'Syne', sans-serif; font-weight: 800; font-size: 2.2rem;
    background: linear-gradient(135deg, #e8e8f0 30%, #7c3aed);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    letter-spacing: -1px; line-height: 1.1;
}
.main-subtitle {
    font-family: 'Space Mono', monospace; font-size: 0.75rem;
    color: #4a4a6a; letter-spacing: 1.5px; text-transform: uppercase; margin-top: 6px;
}
.empty-state {
    display: flex; flex-direction: column; align-items: center;
    justify-content: center; padding: 5rem 2rem; text-align: center;
}
.empty-icon { font-size: 3.5rem; margin-bottom: 1.5rem; opacity: 0.4; }
.empty-title { font-family: 'Syne', sans-serif; font-weight: 700; font-size: 1.2rem; color: #4a4a6a; margin-bottom: 0.5rem; }
.empty-hint { font-family: 'Space Mono', monospace; font-size: 0.7rem; color: #2a2a3e; letter-spacing: 1px; }
[data-testid="stChatMessage"] { background: transparent !important; border: none !important; padding: 0.5rem 0 !important; }
[data-testid="stChatInput"] {
    background: #13131f !important; border: 1px solid #1e1e2e !important; border-radius: 14px !important;
}
[data-testid="stChatInput"]:focus-within {
    border-color: #7c3aed !important; box-shadow: 0 0 0 3px rgba(124,58,237,0.15) !important;
}
[data-testid="stExpander"] {
    background: #0f0f1a !important; border: 1px solid #1e1e2e !important;
    border-radius: 10px !important; margin-top: 0.5rem;
}
[data-testid="stMetric"] { background: #13131f; border: 1px solid #1e1e2e; border-radius: 10px; padding: 0.8rem 1rem; }
[data-testid="stMetricValue"] { font-family: 'Syne', sans-serif !important; font-weight: 800 !important; font-size: 1.8rem !important; color: #7c3aed !important; }
hr { border-color: #1e1e2e !important; }
.source-chip {
    display: inline-flex; align-items: center; gap: 6px;
    background: rgba(124,58,237,0.1); border: 1px solid rgba(124,58,237,0.2);
    border-radius: 6px; padding: 3px 10px;
    font-family: 'Space Mono', monospace; font-size: 0.68rem; color: #7c3aed; margin-bottom: 8px;
}
</style>
""", unsafe_allow_html=True)

# ─── Session State ────────────────────────────────────────────
for key, val in {
    "messages": [], "vectordb_loaded": False,
    "index": None, "chunks": None, "num_chunks": 0
}.items():
    if key not in st.session_state:
        st.session_state[key] = val

# ─── Sidebar ─────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="logo-area">
        <div class="logo-title">DocMind AI</div>
        <div class="logo-sub">RAG · Powered by Groq</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sidebar-label">⚡ Model Stack</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="badge-row">
        <div class="badge"><div class="badge-dot"></div> llama-3.1-8b-instant</div>
        <div class="badge"><div class="badge-dot cyan"></div> all-MiniLM-L6-v2</div>
        <div class="badge"><div class="badge-dot green"></div> FAISS · Top-K: 4</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sidebar-label">📄 Document</div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("", type=["pdf", "txt"], label_visibility="collapsed")

    if uploaded_file:
        if st.button("⚡ Process Document", use_container_width=True):
            with st.spinner("Chunking & indexing..."):
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
                    st.success(f"✅ {len(chunks)} chunks indexed!")
                except Exception as e:
                    st.error(f"❌ {str(e)}")

    st.markdown('<div class="sidebar-label">📊 Index Stats</div>', unsafe_allow_html=True)
    if st.session_state.vectordb_loaded:
        st.markdown('<div class="status-ready">● Vector DB Ready</div>', unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.metric("Chunks Indexed", st.session_state.num_chunks)
    else:
        st.markdown('<div class="status-waiting">● Awaiting Document</div>', unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# ─── Main Area ────────────────────────────────────────────────
st.markdown("""
<div class="main-header">
    <div class="main-title">Ask your documents.</div>
    <div class="main-subtitle">Retrieval-Augmented Generation · Real-time Streaming</div>
</div>
""", unsafe_allow_html=True)

if not st.session_state.messages:
    st.markdown("""
    <div class="empty-state">
        <div class="empty-icon">🧠</div>
        <div class="empty-title">No conversation yet</div>
        <div class="empty-hint">UPLOAD A DOCUMENT → PROCESS → START ASKING</div>
    </div>
    """, unsafe_allow_html=True)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message["role"] == "assistant" and "sources" in message:
            with st.expander("📎 VIEW SOURCE CHUNKS"):
                for i, src in enumerate(message["sources"]):
                    st.markdown(f'<div class="source-chip">◆ SOURCE {i+1} · CHUNK #{src["chunk_id"]}</div>', unsafe_allow_html=True)
                    st.caption(src["text"][:350] + "..." if len(src["text"]) > 350 else src["text"])
                    if i < len(message["sources"]) - 1:
                        st.divider()

if prompt := st.chat_input("Ask anything about your document..."):
    if not st.session_state.vectordb_loaded:
        st.warning("⚠️ Please upload and process a document first!")
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

        with st.expander("📎 VIEW SOURCE CHUNKS"):
            for i, src in enumerate(retrieved):
                st.markdown(f'<div class="source-chip">◆ SOURCE {i+1} · CHUNK #{src["chunk_id"]}</div>', unsafe_allow_html=True)
                st.caption(src["text"][:350] + "..." if len(src["text"]) > 350 else src["text"])
                if i < len(retrieved) - 1:
                    st.divider()

    st.session_state.messages.append({
        "role": "assistant",
        "content": full_response,
        "sources": retrieved
    })
