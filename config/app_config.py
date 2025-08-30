import os
from dotenv import load_dotenv
import streamlit as st
import os

# Access the secret
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]

# Optional: set as environment variable if your code expects it
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

# Load environment variables
load_dotenv()

class AppConfig:
    """Application configuration settings."""
    
    def __init__(self):
        # API Keys
        self.GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
        if not self.GOOGLE_API_KEY:
            raise ValueError("GOOGLE_API_KEY not found in environment variables")
        
        # LLM Settings
        self.LLM_MODEL = "gemini-1.5-flash"
        self.DEFAULT_TEMPERATURE = 0.1
        self.MAX_TOKENS = 2048
        
        # Document Processing Settings
        self.DEFAULT_CHUNK_SIZE = 800
        self.DEFAULT_CHUNK_OVERLAP = 50
        self.MAX_FILE_SIZE_MB = 200
        self.ALLOWED_FILE_TYPES = ["pdf"]
        
        # UI Settings
        self.PAGE_TITLE = "AI Document Assistant"
        self.PAGE_ICON = "📚"
        self.LAYOUT = "wide"
        
        # Session Settings
        self.SESSION_TIMEOUT_HOURS = 24
        self.MAX_QUESTIONS_PER_SESSION = 100
        
        # Processing Settings
        self.MAX_CONCURRENT_UPLOADS = 5
        self.PROCESSING_TIMEOUT_SECONDS = 300
    
    def validate_config(self):
        """Validate configuration settings."""
        errors = []
        
        if not self.GOOGLE_API_KEY:
            errors.append("Google API Key is required")
        
        if self.DEFAULT_CHUNK_SIZE < 100:
            errors.append("Chunk size must be at least 100")
        
        if self.DEFAULT_TEMPERATURE < 0 or self.DEFAULT_TEMPERATURE > 1:
            errors.append("Temperature must be between 0 and 1")
        
        if errors:
            raise ValueError(f"Configuration errors: {', '.join(errors)}")
        
        return True
    
    def get_llm_config(self, temperature=None):
        """
        Get LLM configuration.
        
        Args:
            temperature: Override default temperature
            
        Returns:
            Dictionary with LLM settings
        """
        return {
            "model": self.LLM_MODEL,
            "temperature": temperature or self.DEFAULT_TEMPERATURE,
            "max_tokens": self.MAX_TOKENS
        }
    
    def get_processing_config(self, chunk_size=None, chunk_overlap=None):
        """
        Get document processing configuration.
        
        Args:
            chunk_size: Override default chunk size
            chunk_overlap: Override default chunk overlap
            
        Returns:
            Dictionary with processing settings
        """
        return {
            "chunk_size": chunk_size or self.DEFAULT_CHUNK_SIZE,
            "chunk_overlap": chunk_overlap or self.DEFAULT_CHUNK_OVERLAP,
            "max_file_size_mb": self.MAX_FILE_SIZE_MB,
            "allowed_types": self.ALLOWED_FILE_TYPES
        }