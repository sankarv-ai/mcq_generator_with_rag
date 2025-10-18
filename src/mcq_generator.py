import json
from typing import Dict, Any
from operator import itemgetter

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

from src.config import Config, RESPONSE_JSON
from src.document_processor import DocumentProcessor
from src.embedding_manager import EmbeddingManager

class MCQGenerator:
    """Main class for generating MCQs from documents."""
    
    def __init__(self):
        self.llm = ChatGroq(
            model_name=Config.MODEL_NAME,
            temperature=Config.TEMPERATURE,
            api_key=Config.get_groq_api_key()
        )
        self.document_processor = DocumentProcessor()
        self.embedding_manager = EmbeddingManager()
        self.chain = self._setup_chain()
    
    def _setup_chain(self):
        """Set up the LangChain pipeline for MCQ generation."""
        
        # Define the prompt template
        template = """
        You are an expert MCQ maker. Use the following retrieved text to create a quiz of {number} multiple choice questions for {subject} students in {tone} tone.
        Make sure the questions are not repeated and check all the questions to be conforming to the text as well.
        Retrieved Text: {context}

        Output the response in valid JSON format with double quotes, following the structure of RESPONSE_JSON below. Do not include any other text or markdown outside the JSON block.
        Wrap the JSON output within ```json and ``` markers.
        ### RESPONSE_JSON
        {response_json}
        """
        
        prompt = ChatPromptTemplate.from_template(template)
        
        # Define JSON parser
        parser = JsonOutputParser(pydantic_object={
            "type": "object",
            "patternProperties": {
                "^[0-9]+$": {
                    "type": "object",
                    "properties": {
                        "mcq": {"type": "string"},
                        "options": {
                            "type": "object",
                            "properties": {
                                "a": {"type": "string"},
                                "b": {"type": "string"},
                                "c": {"type": "string"},
                                "d": {"type": "string"}
                            },
                            "required": ["a", "b", "c", "d"]
                        },
                        "correct": {"type": "string"}
                    },
                    "required": ["mcq", "options", "correct"]
                }
            }
        })
        
        # Create the chain
        return (
            {
                "context": itemgetter("text"),
                "number": itemgetter("number"),
                "subject": itemgetter("subject"),
                "tone": itemgetter("tone"),
                "response_json": itemgetter("response_json"),
            }
            | prompt
            | self.llm
            | parser
        )
    
    def generate_quiz_from_pdf(self, pdf_path: str, number: int, subject: str, tone: str) -> Dict[str, Any]:
        """
        Generate MCQs from a PDF document.
        
        Args:
            pdf_path: Path to the PDF file
            number: Number of MCQs to generate
            subject: Subject/topic for the questions
            tone: Difficulty tone (easy, medium, hard)
            
        Returns:
            Dictionary containing generated MCQs
        """
        # Extract text from PDF
        text_data = self.document_processor.extract_text(pdf_path)
        
        # Split text into chunks
        texts = self.embedding_manager.split_text(text_data)
        
        # Create embeddings
        self.embedding_manager.create_embeddings(texts)
        
        # Get retriever
        retriever = self.embedding_manager.get_retriever()
        
        # Get relevant context
        docs = retriever.invoke(subject)
        context = "\n\n".join([doc.page_content for doc in docs])
        
        # Generate quiz
        result = self.chain.invoke({
            "text": context,
            "number": number, 
            "subject": subject,
            "tone": tone,
            "response_json": json.dumps(RESPONSE_JSON, indent=2)
        })
        
        return result
    
    def generate_quiz_from_text(self, text: str, number: int, subject: str, tone: str) -> Dict[str, Any]:
        """
        Generate MCQs from raw text.
        
        Args:
            text: Input text
            number: Number of MCQs to generate
            subject: Subject/topic for the questions
            tone: Difficulty tone (easy, medium, hard)
            
        Returns:
            Dictionary containing generated MCQs
        """
        # Split text into chunks
        texts = self.embedding_manager.split_text(text)
        
        # Create embeddings
        self.embedding_manager.create_embeddings(texts)
        
        # Get retriever
        retriever = self.embedding_manager.get_retriever()
        
        # Get relevant context
        docs = retriever.invoke(subject)
        context = "\n\n".join([doc.page_content for doc in docs])
        
        # Generate quiz
        result = self.chain.invoke({
            "text": context,
            "number": number,
            "subject": subject, 
            "tone": tone,
            "response_json": json.dumps(RESPONSE_JSON, indent=2)
        })
        
        return result