from abc import ABC, abstractmethod

class LivingThingsAbstract(ABC):
    age = 0
    position = {
        "x": 0,
        "y": 0
    }
    
    @abstractmethod
    def grow(self):
        pass
    
    @abstractmethod
    def move(self, x, y):
        pass
    
    @abstractmethod
    def breath(self):
        pass
    
    def eat(self):
        print("Eating")
    
    
class Dog(LivingThingsAbstract):
    
    def grow(self):
        self.age += 1
        
    def move(self, x, y):
        self.position[x] = x
        self.position[y] = y
        
    def breath(self):
        print("Breathing")
    
    
    

dog = Dog()

dog.grow()

print(dog.age)


    