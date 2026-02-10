print("🤖 Mini Chatbot - Day 22")
print("Type 'bye' to exit\n")

while True:
    user_input = input("You: ").lower()

    if user_input == "bye":
        print("Bot: Bye! Have a great day 👋")
        break

    elif "hello" in user_input or "hi" in user_input:
        print("Bot: Hello! How can I help you? 😊")

    elif "your name" in user_input:
        print("Bot: I am a simple Python chatbot 🤖")

    elif "python" in user_input:
        print("Bot: Python is powerful and easy to learn 🔥")

    elif "time" in user_input:
        from datetime import datetime
        print("Bot: Current time is", datetime.now().strftime("%H:%M:%S"))

    elif "help" in user_input:
        print("Bot: You can ask me about Python, time, or just say hello!")

    else:
        print("Bot: Sorry, I didn't understand that 😅")