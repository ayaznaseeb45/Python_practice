

# Define a class named Student
class Student():
    
    # Constructor to initialize the student's name and grade
    def __init__(self, name, grade):
        self.name = name      
        self.grade = grade  

    # Method to display student details
    def student_details(self):
        print(f"{self.name} has grades {self.grade}")

# Create the first Student object
student1 = Student("Ayaz", 45)
# Print the internal dictionary of student1 (shows all attributes)
print(student1.__dict__)   # Output: {'name': 'Ayaz', 'grade': 45}


# Create the second Student object
student2 = Student("Xoxo", 16)
# print(student2.name, student2.grade) 

# Call method to display student1's and 2 details
student1.student_details() 
student2.student_details() 
