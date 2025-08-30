import streamlit as st
import tempfile
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter

class DocumentProcessor:
    """Handles document loading and processing operations."""
    
    def __init__(self):
        pass
    
    def process_files(self, uploaded_files):
        """
        Process uploaded PDF files and extract documents.
        
        Args:
            uploaded_files: List of uploaded Streamlit file objects
            
        Returns:
            List of loaded document objects
        """
        all_docs = []
        
        # Show processing status
        progress_bar = st.progress(0)
        
        for idx, uploaded_file in enumerate(uploaded_files):
            with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_file:
                temp_file.write(uploaded_file.read())
                temp_path = temp_file.name

            loader = PyPDFLoader(temp_path)
            docs = loader.load()
            all_docs.extend(docs)
            
            # Update progress bar
            progress_bar.progress((idx + 1) / len(uploaded_files))
            
            # Clean up temp file
            os.unlink(temp_path)
        
        progress_bar.empty()
        return all_docs
    
    def split_documents(self, documents, chunk_size=800, chunk_overlap=50):
        """
        Split documents into smaller chunks for processing.
        
        Args:
            documents: List of document objects
            chunk_size: Size of each chunk
            chunk_overlap: Overlap between chunks
            
        Returns:
            List of document chunks
        """
        text_splitter = CharacterTextSplitter(
            chunk_size=chunk_size, 
            chunk_overlap=chunk_overlap
        )
        return text_splitter.split_documents(documents)
    
    def get_document_stats(self, documents):
        """
        Get statistics about processed documents.
        
        Args:
            documents: List of document objects
            
        Returns:
            Dictionary with document statistics
        """
        total_chars = sum(len(doc.page_content) for doc in documents)
        total_pages = len(documents)
        
        return {
            'total_pages': total_pages,
            'total_characters': total_chars,
            'avg_page_length': total_chars // total_pages if total_pages > 0 else 0
        }