from typing import Union
from pypdf import PdfReader
import os

class DocumentProcessor:
    """Handles document loading and text extraction."""
    
    @staticmethod
    def extract_text(file_path: str) -> str:
        """
        Extract text from PDF or TXT files.
        
        Args:
            file_path: Path to the document file
            
        Returns:
            Extracted text as string
            
        Raises:
            ValueError: If file type is not supported
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
            
        if file_path.endswith(".pdf"):
            return DocumentProcessor._extract_from_pdf(file_path)
        elif file_path.endswith(".txt"):
            return DocumentProcessor._extract_from_txt(file_path)
        else:
            raise ValueError("Unsupported file type. Please upload PDF or TXT.")
    
    @staticmethod
    def _extract_from_pdf(file_path: str) -> str:
        """Extract text from PDF file."""
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    
    @staticmethod
    def _extract_from_txt(file_path: str) -> str:
        """Extract text from TXT file."""
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()