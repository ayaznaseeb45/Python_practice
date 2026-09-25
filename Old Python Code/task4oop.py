class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.__salary = salary
        self.department = department

    def get_salary(self):
        return self.__salary

    def show_details(self):
        print(f"Name: {self.name}, Salary: {self.get_salary()}, Department: {self.department}")
    
class Manager(Employee):
    def __init__(self, name, salary, department, bonous):
        super().__init__(name , salary , department)
        self.bonous = bonous

    def get_salary(self):
        return super().get_salary() + self.bonous

manager1 = Manager("xyz", 20, "SE" , 5)

# print (manager1.get_salary())

class Intern(Employee):
    def __init__(self, name, salary, department, duration):
        super().__init__(name, salary, department)
        self.duration = duration 
    
    def show_duration(self):
        print(f"Internship Duration: {self.duration} months. ")


intern1 = Intern("Azee", 20000, "IT", 6)

print(intern1.show_duration())