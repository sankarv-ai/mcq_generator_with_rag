import os
from src.mcq_generator import MCQGenerator
from src.utils import print_quiz, save_quiz_to_file

def main():
    # Set your Groq API key
    os.environ["GROQ_API_KEY"] = "your_groq_api_key_here"
    
    # Initialize the generator
    generator = MCQGenerator()
    
    try:
        # Generate quiz from PDF
        quiz = generator.generate_quiz_from_pdf(
            pdf_path="data/sample.pdf",
            number=5,
            subject="English Literature",
            tone="medium"
        )
        
        # Print the quiz
        print("Generated Quiz:")
        print_quiz(quiz)
        
        # Save to file
        save_quiz_to_file(quiz, "generated_quiz.json")
        print("\nQuiz saved to 'generated_quiz.json'")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
