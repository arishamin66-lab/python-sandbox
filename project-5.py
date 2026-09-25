numbers = [2, 5, 2, 8, 5, 9, 1, 8, 3]
numbers2 = []
duplicate = []
for n in numbers:
    if n in numbers2:
        duplicate.append(n)
    else:
        numbers2.append(n)
        
print(duplicate)