student = {
    "name": "Hanish",
    "age": 13,
    "marks": 89,
    "address": {
        "city": "Delhi",
        "state": "Delhi"
    }
}

print(student["name"])
print(student["marks"])
print(student["address"]["city"])
student["course"] = "Python"
student["marks"] = 95

print(student.items())