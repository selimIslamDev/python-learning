

student = {
    "name" : "md salim islam",
    "age" : 25,
    "country" : "bangladesh",
}

print(student["name"])
print(type(student))
student["name"] = "salim in a relationship with sonia"
print(student["name"])
print(student)
student["skills"] = ["python", "java", "c++"]
print(student)
student.pop("skills")
print(student)