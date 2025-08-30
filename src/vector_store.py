from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from config.db_config import DatabaseConfig

class VectorStore:
    """Handles vector database operations."""
    
    def __init__(self):
        self.db_config = DatabaseConfig()
        self.embedding_model = GoogleGenerativeAIEmbeddings(
            model=self.db_config.EMBEDDING_MODEL
        )
    
    def create_database(self, documents):
        """
        Create vector database from documents.
        
        Args:
            documents: List of document chunks
            
        Returns:
            Chroma vector database instance
        """
        db = Chroma.from_documents(
            documents, 
            self.embedding_model, 
            persist_directory=self.db_config.CHROMA_DB_PATH
        )
        return db
    
    def load_database(self):
        """
        Load existing vector database.
        
        Returns:
            Chroma vector database instance
        """
        db = Chroma(
            persist_directory=None,
            embedding_function=self.embedding_model
        )
        return db
    
    def add_documents(self, db, documents):
        """
        Add new documents to existing database.
        
        Args:
            db: Existing Chroma database
            documents: New documents to add
        """
        db.add_documents(documents)
        db.persist()
    
    def search_documents(self, db, query, k=4):
        """
        Search for relevant documents.
        
        Args:
            db: Chroma database
            query: Search query
            k: Number of results to return
            
        Returns:
            List of relevant documents
        """
        return db.similarity_search(query, k=k)
    
    def delete_database(self):
        """Delete the vector database."""
        import shutil
        import os
        
        if os.path.exists(self.db_config.CHROMA_DB_PATH):
            shutil.rmtree(self.db_config.CHROMA_DB_PATH)