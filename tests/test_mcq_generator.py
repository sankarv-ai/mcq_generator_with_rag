import unittest
from unittest.mock import Mock, patch
import os

from src.mcq_generator import MCQGenerator
from src.document_processor import DocumentProcessor

class TestMCQGenerator(unittest.TestCase):
    
    def setUp(self):
        # Mock the Groq API key for testing
        os.environ["GROQ_API_KEY"] = "test_key"
    
    @patch('src.mcq_generator.ChatGroq')
    def test_initialization(self, mock_chat_groq):
        """Test MCQGenerator initialization."""
        generator = MCQGenerator()
        self.assertIsNotNone(generator)
    
    def test_document_processor_pdf_extraction(self):
        """Test PDF text extraction."""
        processor = DocumentProcessor()
        # This would need a sample PDF file for actual testing
        # For now, just test that the method exists
        self.assertTrue(hasattr(processor, 'extract_text'))

if __name__ == '__main__':
    unittest.main()