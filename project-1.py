students = {
    "Ali": 85,
    "Ahmed": 72,
    "Sara": 91,
    "Zain": 64
}

top = students["Ali"]
top_name = "Ali"

low = students["Ali"]
low_name = "Ali"

marks = 0
for key,value in students.items():
    print(f"{key}: {value}")
    marks += value

marks /= len(students)

passed = 0

for key,value in students.items():
    if value > top:
        top = value
        top_name = key
    if value < low:
        low = value
        low_name = key
    if value >= 50:
        passed += 1

print(f"Top Student: {top_name} with marks {top}")
print(f"Lowest Student: {low_name} with marks {low}")
print(f"Average Marks: {marks}")
print(f"Number of Passed Students: {passed}")


