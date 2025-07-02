# polymorphism means Same function name but different behavior 



class Student:
    def __init__(self, name, clas, grade):
        self.name = name
        self.clas = clas
        self.grade = grade

    def student_detail(self):
        # Base class only returns the detail as string (not prints)
        return f"name is {self.name} in class {self.clas} grade {self.grade}%"

class GraduateStudent(Student):
    def __init__(self, name ,clas, grade, stream):
        super().__init__(name, clas, grade)
        self.stream = stream

    def student_detail(self):
        print(f"my name is {self.name}, in class {self.clas}, with grades {self.grade} and stream is {self.stream}")

grStudent = GraduateStudent('zzz', 'bsse', 45, 88)
grStudent.student_detail()
