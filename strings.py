a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''


print(a)

print(a[0])

print(len(a))

print(a[len(a) - 1])

text = "Hello World"

print(text[:5])
print(text[6:8])

print(text[-5:-1:1])

age = 16

print("I am " + str(age) + " years old")

print("I am {0} years old {0}".format(age))


quantity = 3
itemno = 567
price = 49.95

myorder = "I want to pay {2} dollars for {0} pieces of item {1}."

print(myorder.format(quantity, itemno, price))



print("I want to pay 20 dollars for 10 pieces of item 2345.")

print("John said \"I want to go home\" ")

