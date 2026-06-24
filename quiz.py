questions = {
    "What is the capital of India? ": "Delhi",
    "Who developed Python? ": "Guido van Rossum",
    "2 + 2 = ? ": "4",
    "Which keyword is used to define a function in Python? ": "def",
    "What is the extension of Python files? ": ".py"
}

score = 0

for question, answer in questions.items():
    user_answer = input(question)

    if user_answer.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong! Correct answer is:", answer)

print("\nFinal Score:", score, "/", len(questions))