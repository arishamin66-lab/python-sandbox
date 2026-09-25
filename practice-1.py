# Get the user's name and clean up extra whitespace
name = input("Enter your name: ").strip()

# Print the name in uppercase
print(name.upper())

# Print the number of characters in the name
print(len(name))

# Count vowels (both uppercase and lowercase) in the name
vowel = 0
for char in name:
    match char:
        case "A" | "a" | "E" | "e" | "I" | "i" | "O" | "o" | "U" | "u":
            vowel += 1

print(f"Number of vowels in name: {vowel}")

# BUG FIX: without parentheses, Python evaluates "and" before "or", so the
# original condition was actually:
#   name.startswith("A") or (name.startswith("a") and name.endswith("n")) or name.endswith("N")
# which does NOT require both a matching start AND a matching end.
# Grouping the "or" pairs with parentheses makes it check
# (starts with A/a) AND (ends with n/N), as intended.
if (name.startswith("A") or name.startswith("a")) and (name.endswith("n") or name.endswith("N")):
    print("your name starts with A and ends with n")
else:
    print("your name does not starts with A and ends with n")

# Check if the name is a palindrome by comparing it to its reverse
temp = name[::-1]
if name == temp:
    print("Your name is palindrome")
else:
    print("Your name is not palindrome")

# Print how many times each character appears in the name
for char in name:
    print(f"{char}: {name.count(char)}")

# Get a sentence and find the longest word in it
sentence = input("Enter a sentence: ").strip()

ls = sentence.split(" ")
max = 0
longest_word = ""
for word in ls:
    if len(word) > max:
        max = len(word)
        longest_word = word

print(f"Longest word in sentence: {longest_word}")
