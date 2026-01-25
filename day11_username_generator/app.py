import random

print("😎 Username Generator")

name = input("Enter your name: ").strip().lower()

number = random.randint(100, 999)
username = f"{name}_{number}"

print("Your generated username is:")
print(username)