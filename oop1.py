class Student:
    def __init__(self, name, rollnbr, clas):
        self.name = name
        self.clas = clas
        self.rollnbr = rollnbr

    # def student_details(self): 
    #     print(f"{self.name} is in class {self.clas} and roll number is {self.rollnbr}")

# Create object
Student1 = Student('Ayaz', 45, 'BSSE')
print(Student1.__dict__)
Student1.rollnbr = 50
print(Student1.__dict__)

del Student1.rollnbr
print(Student1.__dict__)
Student1.rollnbr = 45
print(Student1.__dict__)


# Call the method correctly
# Student1.student_details()
