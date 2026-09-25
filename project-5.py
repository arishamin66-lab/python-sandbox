numbers = [2, 5, 2, 8, 5, 9, 1, 8, 3]
numbers2 = []   # keeps track of values already seen
duplicate = []  # collects values that show up more than once

for n in numbers:
    if n in numbers2:
        # already seen this value before -> it's a duplicate
        # (guard against adding the same duplicate twice, e.g. if a value
        # appeared 3+ times)
        if n not in duplicate:
            duplicate.append(n)
    else:
        numbers2.append(n)

print(duplicate)
