import os
from pathlib import Path

class DatabaseConfig:
    """Database configuration settings."""
    
    def __init__(self):
        # Base paths
        self.BASE_DIR = Path(__file__).parent.parent
        self.DATA_DIR = self.BASE_DIR / "data"
        self.VECTOR_DB_DIR = self.DATA_DIR / "vector_db"
        self.UPLOADS_DIR = self.DATA_DIR / "uploads"
        
        # Chroma database settings
        self.CHROMA_DB_PATH = str(self.VECTOR_DB_DIR / "chroma_db")
        self.EMBEDDING_MODEL = "models/gemini-embedding-001"
        
        # Create directories if they don't exist
        self._create_directories()
        
        # Vector database settings
        self.COLLECTION_NAME = "document_collection"
        self.SIMILARITY_THRESHOLD = 0.7
        self.MAX_RESULTS = 4
    
    def _create_directories(self):
        """Create necessary directories if they don't exist."""
        self.DATA_DIR.mkdir(exist_ok=True)
        self.VECTOR_DB_DIR.mkdir(exist_ok=True)
        self.UPLOADS_DIR.mkdir(exist_ok=True)
        
        # Create .gitkeep files to ensure directories are tracked in git
        gitkeep_files = [
            self.UPLOADS_DIR / ".gitkeep",
            self.VECTOR_DB_DIR / ".gitkeep"
        ]
        
        for gitkeep in gitkeep_files:
            if not gitkeep.exists():
                gitkeep.touch()
    
    def get_chroma_settings(self):
        """Get Chroma database settings."""
        return {
            "persist_directory": self.CHROMA_DB_PATH,
            "collection_name": self.COLLECTION_NAME
        }
    
    def get_upload_path(self, filename):
        """
        Get full path for uploaded file.
        
        Args:
            filename: Name of the uploaded file
            
        Returns:
            Full path to the uploaded file
        """
        return str(self.UPLOADS_DIR / filename)
    
    def cleanup_uploads(self):
        """Clean up temporary upload files."""
        import shutil
        
        if self.UPLOADS_DIR.exists():
            for file_path in self.UPLOADS_DIR.iterdir():
                if file_path.is_file() and file_path.name != ".gitkeep":
                    file_path.unlink()
    
    def reset_database(self):
        """Reset the vector database by removing all data."""
        import shutil
        
        if Path(self.CHROMA_DB_PATH).exists():
            shutil.rmtree(self.CHROMA_DB_PATH)
            Path(self.CHROMA_DB_PATH).mkdir(parents=True, exist_ok=True)