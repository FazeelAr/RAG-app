import streamlit as st

def apply_custom_css():
    """Apply custom CSS styling to the Streamlit app."""
    
    st.markdown("""
    <style>
        /* Force dark theme compatibility */
        .stApp {
            background-color: transparent;
        }
        
        .main-header {
            text-align: center;
            padding: 2rem 0;
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            color: white !important;
            margin: -1rem -1rem 2rem -1rem;
            border-radius: 10px;
        }
        
        .upload-section {
            background-color: rgba(255, 255, 255, 0.05) !important;
            padding: 2rem;
            border-radius: 10px;
            border: 2px dashed rgba(255, 255, 255, 0.3);
            margin: 1rem 0;
        }
        
        .stat-box {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white !important;
            padding: 1rem;
            border-radius: 10px;
            text-align: center;
            min-width: 150px;
        }
        
        .answer-box {
            background-color: rgba(40, 167, 69, 0.1) !important;
            color: #ffffff !important;
            padding: 1.5rem;
            border-radius: 10px;
            border-left: 5px solid #28a745;
            margin: 1rem 0;
            border: 1px solid rgba(40, 167, 69, 0.3);
        }
        
        .answer-box h4 {
            color: #28a745 !important;
            margin-bottom: 1rem;
        }
        
        .answer-box p {
            color: #ffffff !important;
            font-size: 1.1rem;
            line-height: 1.6;
        }
        
        .source-box {
            background-color: rgba(255, 255, 255, 0.05) !important;
            color: #ffffff !important;
            padding: 1rem;
            border-radius: 8px;
            border-left: 3px solid #6c757d;
            margin: 0.5rem 0;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .source-box h5 {
            color: #87ceeb !important;
            margin-bottom: 0.5rem;
        }
        
        .source-box p {
            color: #ffffff !important;
        }
        
        .source-box small {
            color: #cccccc !important;
        }
        
        .query-section {
            background-color: rgba(255, 255, 255, 0.05) !important;
            padding: 2rem;
            border-radius: 10px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            margin: 1rem 0;
        }
        
        /* Fix text areas and inputs */
        .stTextArea textarea {
            background-color: rgba(255, 255, 255, 0.1) !important;
            color: #ffffff !important;
            border: 1px solid rgba(255, 255, 255, 0.3) !important;
        }
        
        .stTextInput input {
            background-color: rgba(255, 255, 255, 0.1) !important;
            color: #ffffff !important;
            border: 1px solid rgba(255, 255, 255, 0.3) !important;
        }
        
        /* Fix file uploader */
        .uploadedFile {
            background-color: rgba(255, 255, 255, 0.1) !important;
            color: #ffffff !important;
        }
        
        /* General text color fixes */
        .markdown-text-container {
            color: #ffffff !important;
        }
        
        div[data-testid="stMarkdownContainer"] p {
            color: #ffffff !important;
        }
        
        /* Sidebar styling */
        .css-1d391kg {
            background-color: rgba(0, 0, 0, 0.1);
        }
    </style>
    """, unsafe_allow_html=True)