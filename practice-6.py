for i in range(1, 21):
    print(i)

for i in range(2, 51, 2):
    print(i)

for i in range(1, 51, 2):
    print(i)

total = 0
for i in range(1, 101):
    total = total + i
print(total)

number = 5
for i in range(1, 11):
    print(number, "x", i, "=", number * i)

count = 0
for i in range(1, 101):
    if i % 3 == 0:
        count = count + 1
print(count)

total_even = 0
for i in range(1, 101):
    if i % 2 == 0:
        total_even = total_even + i
print(total_even)

num = int(input())
while num >= 0:
    print(num)
    num = int(input())

correct_password = "python123"
user_password = ""
while user_password != correct_password:
    user_password = input()
print("Access granted!")

largest = -1
while True:
    num = int(input())
    if num == -1:
        break
    if num > largest:
        largest = num
print(largest)

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

for i in range(1, 6):
    print("*" * i)

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

num = 17
is_prime = True
if num < 2:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
print(is_prime)

for num in range(1, 101):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)