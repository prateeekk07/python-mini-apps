print("🗳️ Mini Voting System - Day 26\n")

candidates = {
    "1": "Alice",
    "2": "Bob",
    "3": "Charlie"
}

votes = {
    "Alice": 0,
    "Bob": 0,
    "Charlie": 0
}

total_voters = int(input("Enter number of voters: "))

for i in range(1, total_voters + 1):
    print(f"\nVoter {i}")
    for key, name in candidates.items():
        print(f"{key}. {name}")

    choice = input("Enter candidate number: ")

    if choice in candidates:
        selected_candidate = candidates[choice]
        votes[selected_candidate] += 1
        print("✅ Vote recorded!")
    else:
        print("❌ Invalid choice! Vote skipped.")

print("\n📊 Final Results")
for candidate, vote_count in votes.items():
    print(f"{candidate}: {vote_count} votes")

winner = max(votes, key=votes.get)
print(f"\n🏆 Winner is: {winner}")