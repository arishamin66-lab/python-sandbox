data = {"name": "Arish", "age": 18, "grade": "A"}

# Print all keys
for key in data.keys():
    print(key)

# Print all values
for value in data.values():
    print(value)

# Print keys and values together
for key, value in data.items():
    print(f"{key}: {value}")

# Add a new key-value pair
data["marks"] = 75

# Update an existing value
data["age"] = 19

# Check whether a key exists
for key in data:
    if key == "name":
        print("name exists")

# Count the frequency of each character in each value of data2
count = 0
data2 = {"name": "Bilal", "name2": "amin"}
for value in data2.values():
    for char in value:
        print(f"{char}: {value.count(char)}")

students_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 88,
    "Ethan": 95
}

# Find the highest mark
high = 0
for key, value in students_marks.items():
    if value > high:
        high = value

# Print the student(s) who scored the highest mark
for key, value in students_marks.items():
    if value == high:
        print(f"{key}: got the highest marks {value}")

products_prices = {
    "Laptop": 999.99,
    "Smartphone": 699.50,
    "Wireless Headphones": 149.99,
    "Coffee Maker": 79.95,
    "Backpack": 45.00
}

# Print only products costing more than 100
for key, value in products_prices.items():
    if value > 100:
        print(f"{key} : {value}")

number_dictionary = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5
}

# BUG FIX: the original code divided by a hardcoded 5. That only works
# because this particular dictionary happens to have 5 items — if an item
# were added or removed, the average would be wrong. Using
# len(number_dictionary) keeps this correct no matter how many entries exist.
avg = 0
for value in number_dictionary.values():
    avg += value

avg /= len(number_dictionary)
print(avg)

# Build a dictionary from two parallel lists
names = ["Ali", "Ahmed", "Sara"]
marks = [80, 75, 90]

d = dict(zip(names, marks))

print(d)
