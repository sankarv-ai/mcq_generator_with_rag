import os
from typing import Dict, Any
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Configuration settings for the MCQ Generator."""
    
    # Model settings
    MODEL_NAME = "llama-3.3-70b-versatile"
    TEMPERATURE = 0.7
    
    # Text processing settings
    CHUNK_SIZE = 800
    CHUNK_OVERLAP = 200
    
    # Retrieval settings
    SEARCH_K = 3
    SEARCH_TYPE = "similarity"
    
    # Embedding model
    EMBEDDING_MODEL = "all-MiniLM-L6-v2"
    
    # Vector store
    VECTORSTORE_PATH = "./vectorstore"
    
    @classmethod
    def get_groq_api_key(cls) -> str:
        """Get Groq API key from environment variables."""
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY environment variable is not set")
        return api_key

# Response JSON schema for MCQ generation
RESPONSE_JSON = {
    "1": {
        "mcq": "multiple choice question",
        "options": {
            "a": "choice here",
            "b": "choice here", 
            "c": "choice here",
            "d": "choice here",
        },
        "correct": "correct answer",
    }
}