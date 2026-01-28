# import json

# student = {
#     "name": "Ayaz",
#     "age": 20,
#     "subject": "computer"
# }
# print(student.items())
# print(json.dumps(student, indent=4))

# print(student)
# print(type(student))
# print(student.keys())
# print(student.values())
# student["name"] = "Shawaiz"
# print(student)

# student["status"] = "um-married"
# print(student)



import json 

student = {}

for i in range(1,4):
    key = input(f"{i}- Enter name of key: ")
    value = input(f"{i}- Enter its value: ")
    student[key] = value

print(json.dumps(student, indent=4))
