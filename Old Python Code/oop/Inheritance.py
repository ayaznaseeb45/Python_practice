class Student:  # 👨‍🏫 Parent class
    def __init__(self, name, clas, grade):
        self.name = name
        self.clas = clas
        self.grade = grade

    def student_detail(self):
        print(f"Name: {self.name}, Class: {self.clas}, Grade: {self.grade}%")

class GraduateStudent(Student): # Child class inherits from Student
    def __init__(self, name, clas, grade, stream):
        super().__init__(name, clas, grade)  r
        self.stream = stream

    def student_detail(self):
        super().student_detail()  
        print(f"Stream: {self.stream}")

# Creating object of child class
grStudent = GraduateStudent('Ayaz', 'BSSE', 85, 'Computer Science')
grStudent.student_detail()
