import random

print("🎬 Movie Recommender - Day 27\n")

movies = {
    "happy": [
        "The Intern",
        "Zindagi Na Milegi Dobara",
        "The Secret Life of Walter Mitty",
        "3 Idiots"
    ],
    "sad": [
        "The Pursuit of Happyness",
        "A Silent Voice",
        "The Fault in Our Stars",
        "Taare Zameen Par"
    ],
    "motivated": [
        "Rocky",
        "The Social Network",
        "Chak De! India",
        "The Wolf of Wall Street"
    ],
    "action": [
        "John Wick",
        "Mad Max: Fury Road",
        "The Dark Knight",
        "Gladiator"
    ],
    "romantic": [
        "Before Sunrise",
        "Titanic",
        "La La Land",
        "Yeh Jawaani Hai Deewani"
    ]
}

print("Available moods:")
for mood in movies.keys():
    print("-", mood.capitalize())

user_mood = input("\nHow are you feeling today? ").lower()

if user_mood in movies:
    recommendation = random.choice(movies[user_mood])
    print(f"\n🍿 Recommended Movie: {recommendation}")
else:
    print("❌ Sorry, mood not found. Try one from the list.")