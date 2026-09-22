a = set([1,2,3,4,5])
print(a)
a.add(6)
a.remove(3)

for num in a: 
    if num == 4:
        print(f"{num} is present in the set")
        break

b = set([7, 8, 9 , 10])

print(f"Union of a and b: {a.union(b)}")
print(f"Intersection of a and b: {a.intersection(b)}")

c = [10, 20, 30 , 40 ,50]
d = [30 , 40 ,50 ,60 ,70]

for num in c:
    if num in d:
        print(f"{num} appears in both lists")
    
e = set(c)
f = set(d)

print(e.union(f))
        