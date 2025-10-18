from src.mcq_generator import MCQGenerator
import json

def main():
    # Initialize the generator
    generator = MCQGenerator()
    
    # Generate quiz from PDF
    quiz = generator.generate_quiz_from_pdf(
        pdf_path="data/Class_10_English_English_Medium-2024_Edition-www.tntextbooks.in.pdf",
        number=5,
        subject="the last lesson",
        tone="medium"
    )
    
    # Print the results
    print("Generated MCQs:")
    print(json.dumps(quiz, indent=2))
    
    # Save to file
    with open("output/generated_quiz.json", "w") as f:
        json.dump(quiz, f, indent=2)
    print("\nQuiz saved to 'generated_quiz.json'")

if __name__ == "__main__":
    main()