from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document  # Updated import
from typing import List
import os

from src.config import Config

class EmbeddingManager:
    """Manages text embeddings and vector storage."""
    
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name=Config.EMBEDDING_MODEL
        )
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=Config.CHUNK_SIZE,
            chunk_overlap=Config.CHUNK_OVERLAP
        )
        self.vectorstore = None
    
    def create_embeddings(self, texts: List[str]) -> None:
        """
        Create embeddings and store in ChromaDB.
        
        Args:
            texts: List of text chunks to embed
        """
        self.vectorstore = Chroma.from_texts(
            texts=texts,
            embedding=self.embeddings,
            persist_directory=Config.VECTORSTORE_PATH
        )
    
    def get_retriever(self):
        """Get a retriever for similarity search."""
        if self.vectorstore is None:
            raise ValueError("Vector store not initialized. Call create_embeddings first.")
        
        return self.vectorstore.as_retriever(
            search_type=Config.SEARCH_TYPE,
            search_kwargs={"k": Config.SEARCH_K}
        )
    
    def split_text(self, text: str) -> List[str]:
        """
        Split text into chunks.
        
        Args:
            text: Input text to split
            
        Returns:
            List of text chunks
        """
        return self.text_splitter.split_text(text)