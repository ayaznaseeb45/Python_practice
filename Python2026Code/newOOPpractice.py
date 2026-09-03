# # class Car:
# #     brand = "scorpio"

# # car1 = Car()
# # print(car1.brand)


# class Laptop:
#     name = "lenovo"
#     ram = 8
#     price = 100000


# laptop1 = Laptop()
# laptop1.name = "hp"
# laptop1.ram = 16


# laptop2 = Laptop()
# laptop2.price = 150000
# laptop2.name = "dell"

# print(laptop1.name)


# class Car:
#     def __init__(self):
#         print("this is constructor ")
#         print(self)

# car1 = Car()

# class Car():
#     def __init__(self, model, color):
#         self.model = model 
#         self.color = color
    
#     def all_data(self):
#         return f"model name is {self.model} and color is {self.color}"

# class Bike(Car):
#     def __init__(self,model, color, price):
#         super().__init__(model , color)
#         self.price = price 

#     def all_data(self):
#         return f"{super().all_data()} and price is {self.price}"
    



# car1 = Car("BMW", "black")
# print(car1.all_data())  


# bike1 = Bike("Honda", "red", 200)
# print(bike1.all_data())

        

# class Student:
#     def __init__(self, name , listOfMarks):
#         self.name = name 
#         self.listOfMarks = listOfMarks

#     def average(self):
#         sum = 0 
#         for i in self.listOfMarks:
#             sum  = sum + i 
#         return sum / len(self.listOfMarks)

# student1 = Student("Ayaz",[80, 90, 70])
# print(student1.average())


# class Bank:
#     def __init__(self, name , balance):
#         self.name = name
#         self.__balance = balance #this is private variable 

#     def set_balance(self, amount):
#         if amount >=0:
#             self.__balance += amount
#             print(f"Blance {self.__balance} has been updated in your account!")
#         else:
#             print("invalid amount")

#     def get_all_data(self):
#         return f"name of user is {self.name} and its account balnce is {self.__balance}"


# # user1 = Bank("ayaz", 1000)
# # print(user1.name)
# # # print(user1.__balance)
# # print(user1.get_all_data())
# # print("***************")

# # user1.set_balance(500)

   
# # class Animal:
# #     def sound(self):
# #         print("Animal speaking")

# # class Dog(Animal):
# #     def sound(self):
# #         print("Barking")

# # class Cat(Animal):
# #     def sound(self):
# #         print("Meow")



# # x1 = Animal()
# # x1.sound()
# # x2 = Dog()
# # x2.sound()


# class Dog:
#     def sound(self):
#         print("Bark")

# class Cat:
#     def sound(self):
#         print("Meow")

# class Cow:
#     def sound(self):
#         print("Moo")

# animal =  [Dog(), Cat(), Cow() ]

# for x in animal:
#     x.sound()





# class Student:
#     def __init__(self,name ):
#         self._name = name 

# class Xstudent(Student):
#     def show_name(self):
#         print(self._name)

# z = Xstudent("ayaz")
# z.show_name()



# from abc import ABC, abstractmethod

# class Vehical(ABC):
#     @abstractmethod
#     def start(self):
#         pass


# class Bike(Vehical):
#     def start(self):
#         print("Bike is starting")

# z = Bike()
# z.start()



# Design a Banking system using Abstraction where 
# different payment methods exist like
#  Card, Cash, UPI. 
# Each method should implement a common pay() function.

# from abc import ABC, abstractmethod
# class Banking(ABC):
#     @abstractmethod
#     def pay(sself):
#         pass

# class Card(Banking):
#     def pay(self):
#         print("Payment made using Card")

# class Cash(Banking):
#     def pay(self):
#         print("Payment made using Cash")


# class UPI(Banking):
#     def pay(self):
#         print("payment made through UPI")


# x= Cash()
# y= Card()
# z= UPI()
# x.pay()
# y.pay()
# z.pay()


 
# class method 

# class Student():
#     school_name = "ABC School"


#     @classmethod
#     def get_school(cls):
#         return cls.school_name


# print(Student.get_school())

 
# static method 

# class Student():

#     @staticmethod
#     def calculate(a, b):
#         return a + b
    
# print(Student.calculate(10, 20))





# f = open("test.txt", "w")
# f.write("Hello World")
# f.close()


# f = open("test.txt", "r")
# print(f.read())
# f.close()

# f = open("test.txt", "a")
# f.write("\n zzzz")
# f.close()


import os 

if os.path.exists("test.txt"):
    print("file exisit")

else:
    print("file not found")


