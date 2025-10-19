# MCQ Generator with RAG

A powerful AI-powered application that automatically generates multiple-choice questions (MCQs) from educational documents using Retrieval-Augmented Generation (RAG) and Groq's Llama model.

## Project Features

-  PDF Processing: Extract text from PDF textbooks and documents
-  AI-Powered Generation: Uses Groq's Llama 3.3 70B model for intelligent question generation
-  RAG Implementation: Retrieval-Augmented Generation for context-aware question creation
-  Customizable Quizzes: Control number of questions, subject, and difficulty level
-  Structured Output: Returns well-formatted JSON with questions, options, and answers
-  High Performance: Leverages Groq's lightning-fast inference speeds

## Tech Stack

| Component | Technology |
|-----------|------------|
| **AI Model** | Groq + Llama-3.3-70b-versatile |
| **Framework** | LangChain |
| **Vector Store** | ChromaDB |
| **Embeddings** | Sentence Transformers (all-MiniLM-L6-v2) |
| **Text Processing** | PyPDF, LangChain Text Splitters |
| **Language** | Python 3.8+ |

## Installation

1. Clone the repository:
```bash
git clone https://github.com/sankarv-ai/mcq_generator_with_rag.git
cd mcq_generator_with_rag
``` 
2. Install the required LIbraries
```bash
pip install -r requirements.txt
```
3. Create a Folder named data and placed your pdf file inside that folder
```bash
And Provide the pdf relative path in run_mcq.py file
```
5. To run the program
```bash
python run_mcq.py
```
