numbers = (10,20,30,40,50)

for num in numbers:
    print(num)
    
high = max(numbers)
low = min(numbers)

for num in numbers:
    print(f"{num} appears this time: {numbers.count(num)}")
    
inp = int(input("Enter number you want to search in the list: "))

if inp in numbers:
    print(f"{inp} is present in the list")
else:
    print("number is not present in the list")

ls = list(numbers)

ls.append(65)

numbers = tuple(ls)

student = ("Ali", 20, "Computer Science")

name, age , prog = student


def myfunc(num):
    a = 0
    for n in num:
        a += n
    return a

coordinates = (10, 20)
x , y = coordinates
print(x ,y)
