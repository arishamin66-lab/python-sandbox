numbers = [10, 20, 30, 40, 50, 60, 70]

high = max(numbers)
low = min(numbers)

# BUG FIX: the original code did `sum = sum(numbers)`, which overwrites the
# built-in sum() function with an int. If this script did anything with
# sum() afterwards it would crash with "TypeError: 'int' object is not
# callable". Renaming the variable avoids shadowing the builtin.
total = sum(numbers)

even = 0
odd = 0
for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

inp = int(input("Enter number you want to search in the list: "))

if inp in numbers:
    print(f"{inp} is present in the list")
else:
    print("number is not present in the list")

ls2 = [10, -10, 20, -20, 30]

# BUG FIX: removing items from a list while iterating over that same list
# (`for num in ls2: ... ls2.remove(num)`) causes Python to skip elements,
# because the list shrinks and shifts while the loop's internal index keeps
# advancing (e.g. it can skip the element right after a removed one).
# Building a new filtered list instead avoids mutating while iterating.
ls2 = [num for num in ls2 if num >= 0]

ls3 = []
for num in numbers:
    if num > 50:
        ls3.append(num)

ls4 = [1, 1, 3, 4, 3, 4, 2, 2]

# BUG FIX: same mutate-while-iterating problem as above. The original loop
# removed values from ls4 while iterating over it, which unpredictably left
# some duplicates behind. Instead, build a new list that keeps only the
# first occurrence of each value (this also preserves the original order).
unique_ls4 = []
for num in ls4:
    if num not in unique_ls4:
        unique_ls4.append(num)
ls4 = unique_ls4

first_high = max(ls4)
second_high = 0
for num in ls4:
    if num > second_high and num < first_high:
        second_high = num

ls5 = ls4[::-1]

print(f"Highest number in list: {high}")
print(f"Lowest number in list: {low}")
print(f"Sum of all numbers in list: {total}")
print(f"Number of even numbers in list: {even}")
print(f"Number of odd numbers in list: {odd}")
print(f"Number of negative numbers in list: {len(ls2)}")
print(f"Number of numbers greater than 50 in list: {len(ls3)}")
print(f"Number of unique numbers in list: {len(ls4)}")
print(f"Second highest number in list: {second_high}")
print(f"Reversed list: {ls5}")
