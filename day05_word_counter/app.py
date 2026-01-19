print("📝 Word Counter App")

sentence = input("Enter a sentence: ").strip()

if sentence == "":
    print("You entered an empty sentence ❌")
else:
    words = sentence.split()
    word_count = len(words)

    print(f"Total words: {word_count}")