import random

print("🐍 Snake Water Gun Game - Day 23\n")

choices = ["snake", "water", "gun"]
user_score = 0
computer_score = 0
rounds = 5

for i in range(1, rounds + 1):
    print(f"\nRound {i}")
    user_choice = input("Choose snake, water or gun: ").lower()
    computer_choice = random.choice(choices)

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice not in choices:
        print("❌ Invalid choice! Round skipped.")
        continue

    if user_choice == computer_choice:
        print("🤝 It's a tie!")
    elif (
        (user_choice == "snake" and computer_choice == "water") or
        (user_choice == "water" and computer_choice == "gun") or
        (user_choice == "gun" and computer_choice == "snake")
    ):
        print("✅ You win this round!")
        user_score += 1
    else:
        print("💻 Computer wins this round!")
        computer_score += 1

print("\n🏆 Final Score")
print(f"You: {user_score}")
print(f"Computer: {computer_score}")

if user_score > computer_score:
    print("🎉 You won the game!")
elif user_score < computer_score:
    print("😅 Computer won the game!")
else:
    print("🤝 It's a tie game!")