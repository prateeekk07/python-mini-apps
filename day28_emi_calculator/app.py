import random

print("⚔️ Turn-Based Battle Game - Day 29\n")

player_hp = 100
computer_hp = 100

while player_hp > 0 and computer_hp > 0:

    print(f"\nYour HP: {player_hp} | Computer HP: {computer_hp}")
    print("1. Attack")
    print("2. Defend")

    choice = input("Choose your action (1/2): ")

    player_damage = random.randint(10, 25)
    computer_damage = random.randint(10, 25)

    if choice == "1":
        print(f"\nYou attacked and dealt {player_damage} damage!")
        computer_hp -= player_damage
    elif choice == "2":
        print("\nYou defended this turn!")
        computer_damage //= 2
    else:
        print("Invalid choice! You lose your turn.")

    # Computer randomly chooses action
    comp_choice = random.choice(["attack", "defend"])

    if comp_choice == "attack":
        print(f"Computer attacks and deals {computer_damage} damage!")
        player_hp -= computer_damage
    else:
        print("Computer defends this turn!")
        player_damage //= 2

# Final Result
print("\n🏁 Battle Over!")

if player_hp > 0:
    print("🎉 You Won the Battle!")
else:
    print("💀 Computer Won the Battle!")