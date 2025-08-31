import streamlit as st
from datetime import datetime

def render_header():
    """Render the main header of the application."""
    st.markdown("""
    <div class="main-header">
        <h1>📚 AI Document Assistant</h1>
        <p>Upload PDFs and get instant answers powered by RAG technology</p>
    </div>
    """, unsafe_allow_html=True)

def render_sidebar():
    """
    Render sidebar with instructions and settings.
    
    Returns:
        Tuple of (chunk_size, chunk_overlap, temperature)
    """
    with st.sidebar:
        st.markdown("## 📋 How to Use")
        st.markdown("""
        1. **Upload PDFs**: Choose one or more PDF files
        2. **Wait for Processing**: Documents will be processed automatically
        3. **Ask Questions**: Enter your question in the text box
        4. **Get Answers**: Receive AI-powered responses with sources
        """)
        
        st.markdown("## ⚙️ Settings")
        
        # Advanced settings in sidebar
        with st.expander("Advanced Options"):
            chunk_size = st.slider("Chunk Size", 400, 1200, 800, 100)
            chunk_overlap = st.slider("Chunk Overlap", 0, 200, 50, 25)
            temperature = st.slider("AI Temperature", 0.0, 1.0, 0.1, 0.1)
        
        st.markdown("## 📊 Session Stats")
        if 'session_stats' not in st.session_state:
            st.session_state.session_stats = {
                'documents_processed': 0,
                'questions_asked': 0,
                'session_start': datetime.now()
            }
        
        st.metric("Documents Processed", st.session_state.session_stats['documents_processed'])
        st.metric("Questions Asked", st.session_state.session_stats['questions_asked'])
    
    return chunk_size, chunk_overlap, temperature

def render_upload_section():
    """
    Render file upload section.
    
    Returns:
        List of uploaded files
    """
    st.markdown("## 📤 Document Upload")
    
    uploaded_files = st.file_uploader(
        label="Choose PDF files",
        type="pdf",
        accept_multiple_files=True,
        help="Select one or more PDF files to upload. Supported format: PDF only."
    )
    
    return uploaded_files

def render_question_section(uploaded_files):
    """
    Render question input section.
    
    Args:
        uploaded_files: List of uploaded files
        
    Returns:
        Tuple of (query, ask_button, clear_button)
    """
    st.markdown("## 💬 Ask Your Question")
    
    if uploaded_files:
        query = st.text_area(
            "Enter your question here:",
            height=100,
            placeholder="What would you like to know about your documents?",
            help="Ask any question related to the content of your uploaded documents."
        )
        
        col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 2])
        with col_btn1:
            ask_button = st.button("🔍 Ask Question", type="primary")
        with col_btn2:
            clear_button = st.button("🧹 Clear")
            
        return query, ask_button, clear_button
    else:
        st.info("👆 Please upload PDF files first to start asking questions.")
        return None, False, False

def render_stats(uploaded_files, all_docs):
    """
    Render document statistics.
    
    Args:
        uploaded_files: List of uploaded files
        all_docs: List of processed documents
    """
    st.markdown("## 📊 Document Statistics")
    
    col_stat1, col_stat2, col_stat3 = st.columns(3)
    
    with col_stat1:
        st.markdown(f"""
        <div class="stat-box">
            <h3>{len(uploaded_files)}</h3>
            <p>PDFs Uploaded</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_stat2:
        st.markdown(f"""
        <div class="stat-box">
            <h3>{len(all_docs)}</h3>
            <p>Pages Processed</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_stat3:
        total_chars = sum(len(doc.page_content) for doc in all_docs)
        st.markdown(f"""
        <div class="stat-box">
            <h3>{total_chars:,}</h3>
            <p>Characters</p>
        </div>
        """, unsafe_allow_html=True)

def render_answer(result):
    """
    Render the answer and sources.
    
    Args:
        result: Result dictionary from QA chain
    """
    st.markdown("## 🎯 Answer")
    
    # Display answer with better visibility
    st.success("✅ **Answer Found!**")
    
    # Create a container with dark background for better text visibility
    with st.container():
        st.markdown(f"""
        <div class="answer-box">
            <h4>🤖 AI Response:</h4>
            <p><strong>{result["result"]}</strong></p>
        </div>
        """, unsafe_allow_html=True)
    
    # Display sources in an expandable section
    with st.expander(f"📚 View Sources ({len(result['source_documents'])} found)", expanded=False):
        for i, doc in enumerate(result["source_documents"], 1):
            st.markdown(f"""
            <div class="source-box">
                <h5>Source {i}:</h5>
                <p>{doc.page_content[:400]}{'...' if len(doc.page_content) > 400 else ''}</p>     
            </div>
            """, unsafe_allow_html=True)
    
    # Add feedback section
    st.markdown("## 💭 Feedback")
    col_feedback1, col_feedback2 = st.columns(2)
    
    with col_feedback1:
        if st.button("👍 Helpful"):
            st.success("Thank you for your feedback!")
    
    with col_feedback2:
        if st.button("👎 Not Helpful"):
            st.info("Thank you for your feedback! We'll work to improve.")

def render_footer():
    """Render application footer."""
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666; padding: 2rem;'>
        <p>⚡ Powered by LangChain, Google Gemini, and Streamlit</p>
    </div>
    """, unsafe_allow_html=True)