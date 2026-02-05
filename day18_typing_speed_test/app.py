import time

print("⌨️ Typing Speed Test - Day 18\n")

sentence = "Python makes automation easy and powerful"
print("Type the following sentence:\n")
print(sentence)
print()

input("Press Enter when you are ready...")

start_time = time.time()

typed_text = input("\nStart typing here:\n")

end_time = time.time()

time_taken = end_time - start_time
word_count = len(sentence.split())
wpm = (word_count / time_taken) * 60

print("\n📊 Result")
print(f"Time Taken : {time_taken:.2f} seconds")
print(f"Speed      : {wpm:.2f} words per minute")

if typed_text == sentence:
    print("✅ Accuracy: Perfect")
else:
    print("⚠️ Accuracy: Needs improvement")
    