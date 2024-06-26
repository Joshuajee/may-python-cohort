class Dog:
    name = None
    age = None
    weight = 20
    
    print(type(weight))
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def birthday(self):
        self.age = self.age + 1
    
    def bark(self):
        print(self.name, "Woof! Woof!")
        self.bite("Thief")
        
    def bite(self, name):
        print(self.name, "bites", name)


a = Dog("Brain", 13)

b = Dog("Bingo", 4)

a.bark()

b.bark()

a.birthday()

print(a.age)

print(b.age)

print(type(a))

b.bite("Jon")

print(type(b))