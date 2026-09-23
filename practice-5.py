data = {"name": "Arish" , "age": 18, "grade": "A"}
for key in data.keys():
    print(key)
    
for value in data.values():
    print(value)
    
for key , value in data.items():
    print(f"{key}: {value}")
    
data["marks"] = 75

data["age"] = 19

for key in data:
    if key == "name":
        print("name exists")

count = 0
data2 = {"name" : "Bilal" , "name2" : "amin"}
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

high = 0

for key,value in students_marks.items():
    if value > high:
        high = value

for key,value in students_marks.items():
    if value == high:
        print(f"{key}: got the highest marks {value}")
        
products_prices = {
    "Laptop": 999.99,
    "Smartphone": 699.50,
    "Wireless Headphones": 149.99,
    "Coffee Maker": 79.95,
    "Backpack": 45.00
}

for key,value in products_prices.items():
    if value > 100:
        print(f"{key} : {value}")
   
     

number_dictionary = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5
}

avg = 0

for value in number_dictionary.values():
    avg += value
    
avg /= 5
print(avg)

names = ["Ali", "Ahmed", "Sara"]
marks = [80, 75, 90]

d = dict(zip(names,marks))

    
print(d)