list1 = [1, "hello", False, [1, 3]]
list2 = [1, "hello", False, [1, 3]]

list1[0] += 10 

list1[1] = 9.0

print(list1[0])

print(list1)

#[1, "hello", False]
#[False, [1, 3]]
#["hello", False]
#["hello", False, [1, 3]]

print(list2[:3])
print(list2[2:])
print(list2[1:3])
print(list2[1:4])

list2.insert(1, 99)

print(list2)

list2.append("Hello world")

list2.append("Bye")

print(list2)


list3 = [1, 2, 3]
list4 = ("a", "b", "c")

list3.extend(list4)

print(list3)

list3.remove("a")
list3.pop(2)
list3.pop(3)

print(list3)

print(len(list3))

list3.reverse()


print(list3)

list5 = ["apple", "banana", "cherry"]
list6 = ["potatoe", "onion", "banana", "apple"]
output = []
for x in list5:
  for y in list6:
    if (x == y):
      output.append(x)
      print(x)
    #print(x, y)
  
print(output)  

# for i in range(len(list6)):
#   list6[i] = "nothing"
#   print(i)
  
print(list6)

i = 0
while i < len(list6):
  print(list6[i])
  i = i + 1



common = [x for x in list5 if x in list6]

print(common)

for x in list5:
  if x in list6:
    print(x)