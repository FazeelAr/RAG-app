try:
    import pysqlite3
    import sys
    sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")
except ImportError:
    import sqlite3


from dotenv import load_dotenv
import streamlit as st
import os

GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY

from datetime import datetime

from src.document_processor import DocumentProcessor
from src.vector_store import VectorStore
from src.qa_chain import QAChain
from components.styling import apply_custom_css
from components.ui_helpers import (
    render_header, render_sidebar, render_upload_section,
    render_question_section, render_stats, render_answer,
    render_footer
)
from config.app_config import AppConfig
import asyncio

try:
    asyncio.get_running_loop()
except:
    asyncio.set_event_loop(asyncio.new_event_loop())

# Page configuration
st.set_page_config(
    page_title="AI Document Assistant",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom styling
apply_custom_css()

# Initialize session state
if 'session_stats' not in st.session_state:
    st.session_state.session_stats = {
        'documents_processed': 0,
        'questions_asked': 0,
        'session_start': datetime.now()
    }

# Initialize components
doc_processor = DocumentProcessor()
vector_store = VectorStore()
qa_chain = QAChain()

# Render header
render_header()

# Render sidebar
chunk_size, chunk_overlap, temperature = render_sidebar()

# Main content area
col1, col2 = st.columns([1, 2])

with col1:
    uploaded_files = render_upload_section()

with col2:
    query, ask_button, clear_button = render_question_section(uploaded_files)

# Process documents
all_docs = []

if uploaded_files:
    # Process uploaded files
    all_docs = doc_processor.process_files(uploaded_files)
    
    # Update session stats
    st.session_state.session_stats['documents_processed'] = len(uploaded_files)
    
    # Render statistics
    render_stats(uploaded_files, all_docs)
    
    # Build vector database
    with st.spinner('🧠 Building knowledge base...'):
        documents = doc_processor.split_documents(all_docs, chunk_size, chunk_overlap)
        db = vector_store.create_database(documents)
        qa_chain_instance = qa_chain.create_chain(db, temperature)
    
    st.success("✅ Documents processed successfully! You can now ask questions.")
    
    # Handle question answering
    if query and (ask_button or query):
        st.session_state.session_stats['questions_asked'] += 1
        
        with st.spinner('🤔 Thinking...'):
            try:
                result = qa_chain_instance.invoke({"query": query})
                render_answer(result)
                
            except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}")
                st.info("Please try rephrasing your question or check your documents.")

    # Clear functionality
    if clear_button:
        st.session_state.clear()
        st.rerun()

# Render footer
render_footer()