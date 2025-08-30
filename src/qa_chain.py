from langchain.chains import RetrievalQA
from langchain_google_genai import GoogleGenerativeAI
from langchain.globals import set_verbose
from config.app_config import AppConfig

# Set verbose mode for debugging
set_verbose(True)

class QAChain:
    """Handles question-answering chain operations."""
    
    def __init__(self):
        self.config = AppConfig()
    
    def create_chain(self, vector_db, temperature=0.1):
        """
        Create QA chain with vector database.
        
        Args:
            vector_db: Vector database instance
            temperature: LLM temperature setting
            
        Returns:
            RetrievalQA chain instance
        """
        llm = GoogleGenerativeAI(
            model=self.config.LLM_MODEL, 
            temperature=temperature
        )
        
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=vector_db.as_retriever(),
            return_source_documents=True
        )
        
        return qa_chain
    
    def ask_question(self, qa_chain, question):
        """
        Ask a question using the QA chain.
        
        Args:
            qa_chain: RetrievalQA instance
            question: User question
            
        Returns:
            Dictionary with answer and source documents
        """
        try:
            result = qa_chain.invoke({"query": question})
            return {
                'success': True,
                'answer': result['result'],
                'source_documents': result['source_documents'],
                'error': None
            }
        except Exception as e:
            return {
                'success': False,
                'answer': None,
                'source_documents': None,
                'error': str(e)
            }
    
    def format_sources(self, source_documents, max_length=400):
        """
        Format source documents for display.
        
        Args:
            source_documents: List of source documents
            max_length: Maximum length of each source preview
            
        Returns:
            List of formatted source information
        """
        formatted_sources = []
        
        for i, doc in enumerate(source_documents, 1):
            content_preview = doc.page_content[:max_length]
            if len(doc.page_content) > max_length:
                content_preview += "..."
                
            formatted_sources.append({
                'index': i,
                'content': content_preview,
                'metadata': doc.metadata,
                'full_content': doc.page_content
            })
        
        return formatted_sources