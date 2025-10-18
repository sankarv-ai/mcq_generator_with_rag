import json
from typing import Dict, Any

def save_quiz_to_file(quiz: Dict[str, Any], filename: str) -> None:
    """
    Save generated quiz to a JSON file.
    
    Args:
        quiz: Generated quiz dictionary
        filename: Output filename
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(quiz, f, indent=2, ensure_ascii=False)

def print_quiz(quiz: Dict[str, Any]) -> None:
    """
    print the generated quiz.
    
    Args:
        quiz: Generated quiz dictionary
    """
    print(json.dumps(quiz, indent=2))
