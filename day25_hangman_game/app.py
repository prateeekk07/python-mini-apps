import random

print("🎯 Hangman Game - Day 25\n")

words = ["python", "developer", "automation", "challenge", "programming"]
word = random.choice(words)

guessed_letters = []
wrong_attempts = 6

while wrong_attempts > 0:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word.strip())
    print("Wrong attempts left:", wrong_attempts)

    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word correctly!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
    elif guess in word:
        guessed_letters.append(guess)
        print("✅ Correct guess!")
    else:
        guessed_letters.append(guess)
        wrong_attempts -= 1
        print("❌ Wrong guess!")

if wrong_attempts == 0:
    print(f"\n💀 Game Over! The correct word was '{word}'.")