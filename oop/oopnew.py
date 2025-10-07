class Student():

    def __init__(self, name, grade, age, percentage, team):
        self.name = name
        self.grade = grade
        self.age = age 
        self.percentage = percentage
        self.team = team
    
    def student_details(self):
        print(f"{self.name} has grades {self.grade}")


team1 = 'King'
team2 = 'Spider'

student1 = Student("ayaz", 45 , 25, 99, team1)
student2 = Student("shawaiz", 45 , 25, 99, team2)



print(student1.__dict__)
student1.student_details()

# # add new percentage 
# student1.percentage = 22
# print(student1.__dict__)

# # delete percentage
# del student1.percentage
# print(student1.__dict__)
