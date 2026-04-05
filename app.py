import os
import streamlit as st
from src.retriever import retrieve_relevant_chunks, format_context
from src.generator import generate_streaming_response

st.set_page_config(
    page_title="DocMind AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Manrope:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Manrope', sans-serif;
    background-color: #080810;
    color: #e2e2f0;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 2.5rem; max-width: 100%; }
::-webkit-scrollbar { width: 3px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: #2a2a4a; border-radius: 2px; }
section[data-testid="stSidebar"] { background: #0d0d1a; border-right: 1px solid #16162a; }
section[data-testid="stSidebar"] .block-container { padding: 1.8rem 1.2rem; }
.brand { display: flex; flex-direction: column; align-items: center; padding-bottom: 1.4rem; border-bottom: 1px solid #16162a; margin-bottom: 1.4rem; }
.brand-icon { width: 44px; height: 44px; background: linear-gradient(135deg, #6d28d9, #0ea5e9); border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.3rem; margin-bottom: 10px; box-shadow: 0 0 24px rgba(109,40,217,0.35); }
.brand-name { font-family: 'Manrope', sans-serif; font-weight: 800; font-size: 1.15rem; color: #f0f0ff; letter-spacing: -0.3px; }
.brand-tag { font-family: 'DM Mono', monospace; font-size: 0.6rem; color: #3a3a5a; letter-spacing: 2.5px; text-transform: uppercase; margin-top: 2px; }
.section-label { font-family: 'DM Mono', monospace; font-size: 0.6rem; color: #3a3a5a; letter-spacing: 2.5px; text-transform: uppercase; margin-bottom: 8px; margin-top: 16px; }
.model-card { background: #111120; border: 1px solid #1a1a2e; border-radius: 10px; padding: 10px 12px; margin-bottom: 6px; display: flex; align-items: center; gap: 10px; }
.model-dot { width: 7px; height: 7px; border-radius: 50%; flex-shrink: 0; }
.dot-purple { background: #6d28d9; box-shadow: 0 0 6px #6d28d9; }
.dot-blue { background: #0ea5e9; box-shadow: 0 0 6px #0ea5e9; }
.dot-green { background: #10b981; box-shadow: 0 0 6px #10b981; }
.model-text { font-family: 'DM Mono', monospace; font-size: 0.72rem; color: #8888aa; }
.status-badge { display: inline-flex; align-items: center; gap: 6px; border-radius: 20px; padding: 5px 12px; font-family: 'DM Mono', monospace; font-size: 0.68rem; }
.status-ready { background: rgba(16,185,129,0.08); border: 1px solid rgba(16,185,129,0.25); color: #10b981; }
.status-waiting { background: rgba(245,158,11,0.08); border: 1px solid rgba(245,158,11,0.25); color: #f59e0b; }
[data-testid="stFileUploader"] { background: #111120; border: 1px dashed #1e1e35; border-radius: 10px; padding: 4px; }
[data-testid="stFileUploader"]:hover { border-color: #6d28d9; }
.stButton > button { background: linear-gradient(135deg, #6d28d9, #4f46e5) !important; color: white !important; border: none !important; border-radius: 10px !important; font-family: 'Manrope', sans-serif !important; font-weight: 600 !important; font-size: 0.83rem !important; padding: 0.55rem 1rem !important; transition: all 0.2s ease !important; }
.stButton > button:hover { transform: translateY(-1px) !important; box-shadow: 0 6px 18px rgba(109,40,217,0.45) !important; }
[data-testid="stMetric"] { background: #111120; border: 1px solid #1a1a2e; border-radius: 10px; padding: 0.8rem 1rem; }
[data-testid="stMetricValue"] { font-family: 'Manrope', sans-serif !important; font-weight: 800 !important; font-size: 1.6rem !important; color: #6d28d9 !important; }
[data-testid="stMetricLabel"] { font-family: 'DM Mono', monospace !important; font-size: 0.62rem !important; color: #3a3a5a !important; letter-spacing: 1.5px !important; text-transform: uppercase !important; }
.hero { padding: 2.5rem 0 2rem 0; border-bottom: 1px solid #16162a; margin-bottom: 2rem; }
.hero-title { font-family: 'Manrope', sans-serif; font-weight: 800; font-size: 2.6rem; color: #f0f0ff; letter-spacing: -1.5px; line-height: 1.1; }
.hero-title span { background: linear-gradient(135deg, #6d28d9, #0ea5e9); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.hero-sub { font-family: 'DM Mono', monospace; font-size: 0.72rem; color: #3a3a5a; letter-spacing: 2px; text-transform: uppercase; margin-top: 8px; }
.empty-wrap { display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 4rem 2rem; text-align: center; gap: 16px; }
.empty-glyph { width: 64px; height: 64px; background: #111120; border: 1px solid #1a1a2e; border-radius: 16px; display: flex; align-items: center; justify-content: center; font-size: 1.8rem; }
.empty-title { font-family: 'Manrope', sans-serif; font-weight: 700; font-size: 1.05rem; color: #3a3a5a; }
.empty-steps { display: flex; gap: 8px; align-items: center; flex-wrap: wrap; justify-content: center; }
.step-pill { background: #111120; border: 1px solid #1a1a2e; border-radius: 20px; padding: 4px 12px; font-family: 'DM Mono', monospace; font-size: 0.65rem; color: #4a4a6a; letter-spacing: 1px; }
.step-arrow { color: #2a2a4a; font-size: 0.8rem; }
[data-testid="stChatMessage"] { background: transparent !important; border: none !important; padding: 0.4rem 0 !important; }
[data-testid="stChatInput"] { background: #111120 !important; border: 1px solid #1a1a2e !important; border-radius: 12px !important; }
[data-testid="stChatInput"]:focus-within { border-color: #6d28d9 !important; box-shadow: 0 0 0 3px rgba(109,40,217,0.12) !important; }
[data-testid="stExpander"] { background: #0d0d1a !important; border: 1px solid #16162a !important; border-radius: 10px !important; margin-top: 6px; }
.source-tag { display: inline-flex; align-items: center; gap: 5px; background: rgba(109,40,217,0.08); border: 1px solid rgba(109,40,217,0.18); border-radius: 5px; padding: 2px 8px; font-family: 'DM Mono', monospace; font-size: 0.65rem; color: #6d28d9; margin-bottom: 6px; }
hr { border-color: #16162a !important; }
</style>
""", unsafe_allow_html=True)

for key, val in {
    "messages": [], "vectordb_loaded": False,
    "index": None, "chunks": None, "num_chunks": 0
}.items():
    if key not in st.session_state:
        st.session_state[key] = val

with st.sidebar:
    st.markdown("""
    <div class="brand">
        <div class="brand-icon">🧠</div>
        <div class="brand-name">DocMind AI</div>
        <div class="brand-tag">RAG · Groq · FAISS</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-label">Model Stack</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="model-card"><div class="model-dot dot-purple"></div><span class="model-text">llama-3.1-8b-instant</span></div>
    <div class="model-card"><div class="model-dot dot-blue"></div><span class="model-text">all-MiniLM-L6-v2</span></div>
    <div class="model-card"><div class="model-dot dot-green"></div><span class="model-text">FAISS · Top-K: 4</span></div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-label">Document</div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload file", type=["pdf", "txt"], label_visibility="collapsed")

    if uploaded_file:
        if st.button("Process Document", use_container_width=True):
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
                    st.success(f"Done! {len(chunks)} chunks indexed.")
                except Exception as e:
                    st.error(f"Error: {str(e)}")

    st.markdown('<div class="section-label">Index Stats</div>', unsafe_allow_html=True)
    if st.session_state.vectordb_loaded:
        st.markdown('<div class="status-badge status-ready">● Vector DB Ready</div>', unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.metric("Chunks Indexed", st.session_state.num_chunks)
    else:
        st.markdown('<div class="status-badge status-waiting">● Awaiting Document</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

st.markdown("""
<div class="hero">
    <div class="hero-title">Ask your <span>documents.</span></div>
    <div class="hero-sub">Retrieval-Augmented Generation · Real-time Streaming</div>
</div>
""", unsafe_allow_html=True)

if not st.session_state.messages:
    st.markdown("""
    <div class="empty-wrap">
        <div class="empty-glyph">🧠</div>
        <div class="empty-title">No conversation yet</div>
        <div class="empty-steps">
            <span class="step-pill">Upload doc</span>
            <span class="step-arrow">→</span>
            <span class="step-pill">Process</span>
            <span class="step-arrow">→</span>
            <span class="step-pill">Ask anything</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message["role"] == "assistant" and "sources" in message:
            with st.expander("View source chunks"):
                for i, src in enumerate(message["sources"]):
                    st.markdown(f'<div class="source-tag">Source {i+1} · Chunk #{src["chunk_id"]}</div>', unsafe_allow_html=True)
                    st.caption(src["text"][:300] + "..." if len(src["text"]) > 300 else src["text"])
                    if i < len(message["sources"]) - 1:
                        st.divider()

if prompt := st.chat_input("Ask anything about your document..."):
    if not st.session_state.vectordb_loaded:
        st.warning("Please upload and process a document first.")
        st.stop()

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        retrieved = retrieve_relevant_chunks(
            prompt, st.session_state.index, st.session_state.chunks
        )
        context = format_context(retrieved)

        placeholder = st.empty()
        full_response = ""
        try:
            for token in generate_streaming_response(prompt, context):
                full_response += token
                placeholder.markdown(full_response + "▌")
            placeholder.markdown(full_response)
        except Exception as e:
            full_response = f"Error: {str(e)}"
            placeholder.markdown(full_response)

        with st.expander("View source chunks"):
            for i, src in enumerate(retrieved):
                st.markdown(f'<div class="source-tag">Source {i+1} · Chunk #{src["chunk_id"]}</div>', unsafe_allow_html=True)
                st.caption(src["text"][:300] + "..." if len(src["text"]) > 300 else src["text"])
                if i < len(retrieved) - 1:
                    st.divider()

    st.session_state.messages.append({
        "role": "assistant",
        "content": full_response,
        "sources": retrieved
    })
