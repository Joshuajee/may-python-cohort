class Person:
    __fullname = None
    __height = None
    __age = None
    
    def __init__(self, fullname, height, age):
        self.__fullname = fullname
        self.__height = height
        self.__age = age
        
    def setFullname(self, fullname):
        self.__fullname = fullname
        
    def getFullName(self):
        return self.__fullname
        
        
        
john = Person("Jon Doe", 178, 18)

print(john.getFullName())