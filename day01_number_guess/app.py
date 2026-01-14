import random

secret_number = random.randint(1, 20)
attempts = 0

print("🎯 Welcome to Number Guess Game!")
print("Guess a number between 1 and 20")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess > secret_number:
        print("Too high 📈")
    elif guess < secret_number:
        print("Too low 📉")
    else:
        print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
        break