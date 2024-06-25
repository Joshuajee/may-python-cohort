sets = {1, 3, 5, 6, 7, 3, 3, 3, "3", "3"}

print(sets)

sets.add("ball")

print(sets)

sets.update({10, 20})

print(sets)

set2 = {10, 20, 2, 4, 3, 1}

print(sets.union(set2))

print(sets.intersection(set2))