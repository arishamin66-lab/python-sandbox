# Create a set of numbers
a = set([1, 2, 3, 4, 5])
print(a)

# Add and remove elements from the set
a.add(6)
a.remove(3)

# Check whether a value exists in the set
for num in a:
    if num == 4:
        print(f"{num} is present in the set")
        break

b = set([7, 8, 9, 10])

# Union: all values from both sets, no duplicates
print(f"Union of a and b: {a.union(b)}")
# Intersection: only values present in both sets
print(f"Intersection of a and b: {a.intersection(b)}")

c = [10, 20, 30, 40, 50]
d = [30, 40, 50, 60, 70]

# Find values that appear in both lists
for num in c:
    if num in d:
        print(f"{num} appears in both lists")

# Using sets to find all unique values appearing in either list
e = set(c)
f = set(d)

print(e.union(f))
