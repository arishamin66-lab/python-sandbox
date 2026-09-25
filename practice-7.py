def print_hello_world():
    # Simple function with no return value, just prints a greeting
    print("Hello, World!")


def greet_person(name):
    # Greets a specific person by name
    print(f"Hello, {name}!")


def sum_two_numbers(a, b):
    # Returns the sum of two numbers
    return a + b


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    # Guard against division by zero
    if b == 0:
        return "Division by zero is not allowed"
    return a / b


def is_even(number):
    return number % 2 == 0


def find_largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


def find_largest_in_list(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


def count_even_numbers(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count


def is_palindrome(text):
    # Compare the lowercased text to its reverse
    cleaned_text = text.lower()
    return cleaned_text == cleaned_text[::-1]


def get_top_student(students):
    # students is a dict of {name: score}; find the name with the highest score
    if not students:
        return None
    top_student = None
    highest_score = float('-inf')
    for name, score in students.items():
        if score > highest_score:
            highest_score = score
            top_student = name
    return top_student


def get_unique_values(items):
    # Builds a new list keeping only the first occurrence of each item
    # (safe because it never mutates the list being iterated over)
    unique_items = []
    for item in items:
        if item not in unique_items:
            unique_items.append(item)
    return unique_items
