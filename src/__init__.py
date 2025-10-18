"""
MCQ Generator Package

A powerful application for generating multiple-choice questions from documents
using Groq's Llama model and LangChain.
"""

__version__ = "1.0.0"
__author__ = "sankar"
__email__ = "sankarvnk.ai@gmail.com"

from .mcq_generator import MCQGenerator
from .document_processor import DocumentProcessor
from .embedding_manager import EmbeddingManager
from .config import Config

__all__ = [
    "MCQGenerator",
    "DocumentProcessor", 
    "EmbeddingManager",
    "Config"
]