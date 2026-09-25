numbers = (10, 20, 30, 40, 50)

# Print each number in the tuple
for num in numbers:
    print(num)

high = max(numbers)
low = min(numbers)

# Print how many times each value appears in the tuple
for num in numbers:
    print(f"{num} appears this time: {numbers.count(num)}")

inp = int(input("Enter number you want to search in the list: "))

if inp in numbers:
    print(f"{inp} is present in the list")
else:
    print("number is not present in the list")

# Tuples are immutable, so to add a value we convert to a list,
# modify it, then convert back to a tuple
ls = list(numbers)
ls.append(65)
numbers = tuple(ls)

student = ("Ali", 20, "Computer Science")

# Unpack the tuple into separate variables
name, age, prog = student


def myfunc(num):
    # Accepts a tuple/list of numbers and returns their sum
    a = 0
    for n in num:
        a += n
    return a


coordinates = (10, 20)
x, y = coordinates
print(x, y)
