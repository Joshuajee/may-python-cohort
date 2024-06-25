student = {
    "id": "8870890",
    "name": "John Baller",
    "course": "Python",
    "duration": 3,
}


student.update({"duration": 4, "age": 6})

student["grade"] = "A"

print(student)

student.pop("grade")

print(student)

student.popitem()

print(student)

print(student["name"])

print(student.keys())


for x in student.keys():
    print(x, ":", student.get(x))