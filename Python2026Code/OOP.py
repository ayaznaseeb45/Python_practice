# # class Vehicle:
# #     color = "Red"
# #     speed = 100

# # obj = Vehicle()
# # print(obj.color)



# class Laptop:
#     brand = "default name Hp"
#     ram = "default is 8GB"
#     color = "default Blue"

# laptop1 = Laptop()
# laptop1.brand = "Lenovo"
# laptop1.color = "White"
# laptop1.color = "gray"
# laptop1.ram = "8Gb"

# print(f"laptop1 data: ", laptop1.brand)

# laptop2 = Laptop()
# laptop2.brand = "IBM"
# laptop2.color = "Black"
# laptop2.ram = "24GB"
# print(f"laptop2 data: ", laptop2.brand)



class Car:
    
    def __init__(self, userbrand, usermodel):
        self.brand = userbrand
        self.model = usermodel
    
    def all_data(self):
        return f"brand name is {self.brand} and model name is {self.model}"

car1 = Car("BMW", 2025)
print(car1.all_data())