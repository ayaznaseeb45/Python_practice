#Parent class 
class Student():

    def __init__(self, name, grade, age ):
        self.name = name
        self.grade = grade
        self.age = age

    def student_details(self):
        print(f"{self.name} has grades {self.grade} age is {self.age} ")

student1 = Student("ayaz", 45 , 25,)
student2 = Student("shawaiz", 45 , 25,)

# print(student1.__dict__)
# print(student1.get_age())

# Child class 

class GraduateStudent(Student):
    def __init__(self, name, grade, age, stream):
        super().__init__(name, grade, age)
        self.stream = stream

    def student_details(self):
        super().student_details()
        print(f"and strem is {self.stream}")

student3 = GraduateStudent("xyz", 45 , 45 , "MQM")
print(student3.stream)
print(student3.__dict__)