print("🧠 Simple Python Quiz App")

questions = {
    "What is the capital of India?": "delhi",
    "Which language is used for web development?": "python",
    "What does CPU stand for?": "central processing unit",
    "Which keyword is used to define a function in Python?": "def",
    "What is 5 + 7?": "12"
}

score = 0

for question, correct_answer in questions.items():
    print("\n" + question)
    user_answer = input("Your answer: ").lower().strip()

    if user_answer == correct_answer:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer is: {correct_answer}")

print("\n🎉 Quiz Completed!")
print(f"Your final score: {score}/{len(questions)}")