# my_dict = {
#     "name": "Ayaz",
#     "RollNo": "45"
# }

# print(my_dict)         
# print(type(my_dict))   


# person = dict(name="ayaz", rollNo="45")

# print(person)


# student = {
#     1 :"xyz",
#     "name":"ayaz",
#     "class":"SE 7th",
#     "xoxo":"xox"

# }

# print(student.keys())
# print(student.values())
# print(student.items())
# print(student.get("name"))
# student["email"] = "ayaz@gmail.com"
# print(student)

# student = {
#     1 :"xyz",
#     "name":"ayaz",
#     "class":"SE 7th",
#     "xoxo":"xox"

# }

# # for key, value in student.items():
#     # print(key, value)
# for value in student:
#     print(student[value])




main_student= {
    "student1": {
        "name": "Ayaz",
        "role": "Backend Developer",
        "skills": "python",


    },
    "student2": {
        "name": "Kafeel",
        "role": "Frontend Developer",
        "skills": "JS",
        "age":20
    }
}

print(main_student["student2"])