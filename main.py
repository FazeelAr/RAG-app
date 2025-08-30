from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import tempfile

import asyncio

# 🔧 Ensure event loop exists for Streamlit thread
try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_google_genai import GoogleGenerativeAI

from langchain.globals import set_verbose

# Enable verbose mode
set_verbose(True)

st.title("RAG powered AI application")

uploaded_files = st.file_uploader(
    label="Upload PDF files",
    type="pdf",
    accept_multiple_files=True
)

all_docs = []

if uploaded_files:
    for uploaded_file in uploaded_files:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_file:
            temp_file.write(uploaded_file.read())
            temp_path = temp_file.name

        loader = PyPDFLoader(temp_path)
        docs = loader.load()
        all_docs.extend(docs)

    st.write(f"Loaded {len(all_docs)} pages from {len(uploaded_files)} PDFs.")

    # Split docs
    text_splitter = CharacterTextSplitter(chunk_size=800, chunk_overlap=0)
    documents = text_splitter.split_documents(all_docs)

    # Embedding model
    embedding_model = GoogleGenerativeAIEmbeddings(model='models/gemini-embedding-001')

    # Vector DB
    db = Chroma.from_documents(documents, embedding_model)
    

    # Initialize LLM
    llm = GoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)

    # Create RAG chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=db.as_retriever(),
        return_source_documents=True
    )

    query = st.text_input("Enter your question")

    if query:
        result = qa_chain.invoke({"query": query})
        
        # Show answer
        st.write("**Answer:**", result["result"])
        
        # Show sources
        for i, doc in enumerate(result["source_documents"], 1):
            st.write(f"**Source {i}:** {doc.page_content[:300]}...")
