import random

print("🧮 Math Quiz Generator - Day 21\n")

score = 0
total_questions = 5

for i in range(1, total_questions + 1):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(["+", "-", "*"])

    if operator == "+":
        correct_answer = num1 + num2
    elif operator == "-":
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2

    print(f"Q{i}: What is {num1} {operator} {num2}?")
    user_answer = input("Your answer: ")

    if user_answer.isdigit() and int(user_answer) == correct_answer:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer is {correct_answer}\n")

print("📊 Quiz Completed!")
print(f"Your Score: {score}/{total_questions}")