def my_func():
    print("Hello,")
    print("How are you doing, today")



def greeting(name):
    print("Goodmorning", name)

greeting("Franklin")
greeting("Joshua")

person = "Mark"

greeting(person)


def fullname(fname, lname):
    firstname = fname.strip().lower().capitalize()
    lastname =  lname.lower().strip().capitalize()
    print(firstname + " " + lastname)
    
fullname("  johN", "    DoE   ")

fullname("  michaeL", "    smit   ")

def add(x, y):
    print(x + y)
    
add(10, 40)


def get_minimum(*nums):
    print(nums)
    print(min(nums))
    
get_minimum(8, 4, 9, 6)

print("Hello")