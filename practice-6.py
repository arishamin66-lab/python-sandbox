# Print numbers 1 to 20
for i in range(1, 21):
    print(i)

# Print even numbers from 2 to 50
for i in range(2, 51, 2):
    print(i)

# Print odd numbers from 1 to 50
for i in range(1, 51, 2):
    print(i)

# Sum of numbers from 1 to 100
total = 0
for i in range(1, 101):
    total = total + i
print(total)

# Multiplication table for a fixed number
number = 5
for i in range(1, 11):
    print(number, "x", i, "=", number * i)

# Count numbers between 1 and 100 divisible by 3
count = 0
for i in range(1, 101):
    if i % 3 == 0:
        count = count + 1
print(count)

# Sum of even numbers between 1 and 100
total_even = 0
for i in range(1, 101):
    if i % 2 == 0:
        total_even = total_even + i
print(total_even)

# Keep asking for numbers until the user enters a negative one
num = int(input())
while num >= 0:
    print(num)
    num = int(input())

# Keep asking for a password until the correct one is entered
correct_password = "python123"
user_password = ""
while user_password != correct_password:
    user_password = input()
print("Access granted!")

# Find the largest number entered; stop when the user enters -1
largest = -1
while True:
    num = int(input())
    if num == -1:
        break
    if num > largest:
        largest = num
print(largest)

# Count how many of 5 entered numbers are positive, negative, or zero
positives = 0
negatives = 0
zeros = 0
for i in range(5):
    num = int(input())
    if num > 0:
        positives = positives + 1
    elif num < 0:
        negatives = negatives + 1
    else:
        zeros = zeros + 1
print(positives, negatives, zeros)

# Print a triangle of asterisks
for i in range(1, 6):
    print("*" * i)

# Print an increasing number pattern (1 / 12 / 123 / 1234 / 12345)
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# Check whether a single number is prime
num = 17
is_prime = True
if num < 2:
    is_prime = False
else:
    # IMPROVEMENT: only need to check divisors up to sqrt(num), since any
    # factor larger than that would have a matching factor smaller than it
    # already found. This avoids unnecessary checks for large numbers.
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
print(is_prime)

# Print all prime numbers between 1 and 100 (same sqrt optimization)
for num in range(1, 101):
    if num > 1:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
