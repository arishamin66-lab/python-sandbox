name = input("Enter your name: ").strip()

print(name.upper())
print(len(name))
vowel = 0
for char in name:
    match char:
        case "A" | "a" | "E" | "e" | "I" | "i" | "O" | "o" | "U" | "u":
            vowel += 1

print(f"Number of vowels in name: {vowel}")

if name.startswith("A") or name.startswith("a") and name.endswith("n") or name.endswith("N"):
    print("your name starts with A and ends with n")
else:
    print("your name does not starts with A and ends with n")

temp = name[::-1]
if name == temp:
    print("Your name is palindrome")
else:
    print("Your name is not palindrome")

for char in name:
    print(f"{char}: {name.count(char)}")

sentence = input("Enter a sentence: ").strip()

ls = sentence.split(" ")
max = 0
longest_word = ""
for word in ls:
    if len(word) > max:
        max = len(word)
        longest_word = word

print(f"Longest word in sentence: {longest_word}")