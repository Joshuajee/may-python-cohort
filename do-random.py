import random


print(random.randint(100000, 999999))

fruits = ["apple", "banana", "orange", "mango"]

print(random.choice(fruits))

print(random.choices(fruits, k=3))