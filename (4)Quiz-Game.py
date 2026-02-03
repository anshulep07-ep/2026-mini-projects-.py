import json

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Paris", "Venice", "Milan"],
        "answer": 1
    },
    {
        "question": "Which language is used for AI?",
        "options": ["HTML", "Python", "CSS", "SQL"],
        "answer": 1
    }
]

def run_quiz():
    score = 0

    for q in questions:
        print("\n" + q["question"])
        for i, option in enumerate(q["options"]):
            print(f"{i + 1}. {option}")

        choice = int(input("Your answer: ")) - 1

        if choice == q["answer"]:
            score += 1

    print(f"\nFinal Score: {score}/{len(questions)}")

run_quiz()