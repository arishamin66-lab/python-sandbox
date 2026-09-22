numbers = [10,20,30,40,50, 60 ,70]

high = max(numbers)
low = min(numbers)
sum = sum(numbers)
even = 0
odd =0
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

for num in ls2:
    if num < 0:
        ls2.remove(num)

ls3 = []
for num in numbers:
    if num > 50:
        ls3.append(num)

ls4 = [1 ,1 ,3 ,4 ,3 ,4 ,2 ,2]

for num in ls4:
    if ls4.count(num) > 1:
        ls4.remove(num)

first_high = max(ls4)
second_high = 0
for num in ls4:
    if num > second_high and num < first_high:
        second_high = num

ls5 = ls4[::-1]

print(f"Highest number in list: {high}")
print(f"Lowest number in list: {low}")
print(f"Sum of all numbers in list: {sum}")
print(f"Number of even numbers in list: {even}")
print(f"Number of odd numbers in list: {odd}")
print(f"Number of negative numbers in list: {len(ls2)}")
print(f"Number of numbers greater than 50 in list: {len(ls3)}")
print(f"Number of unique numbers in list: {len(ls4)}")
print(f"Second highest number in list: {second_high}")
print(f"Reversed list: {ls5}")
