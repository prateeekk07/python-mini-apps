print("🔍 Text Search Tool - Day 19\n")

filename = "sample.txt"
search_word = input("Enter word to search: ").lower()

count = 0
line_numbers = []

with open(filename, "r") as file:
    for line_no, line in enumerate(file, start=1):
        if search_word in line.lower():
            count += line.lower().count(search_word)
            line_numbers.append(line_no)

print("\n📊 Search Result")
print(f"Word found {count} times")

if line_numbers:
    print("Found in lines:", line_numbers)
else:
    print("Word not found in file")