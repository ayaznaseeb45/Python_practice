# class Vehicle:
#     def __init__(self, price):
#         self.__name = "BMW"     # private & fixed brand
#         self.price = price

#     @property
#     def brand(self):
#         # read-only brand (cannot be changed)
#         return self.__name

#     def get_data(self):
#         return f"Brand {self.brand}, Price {self.price}"


# class Car(Vehicle):
#     def __init__(self, price, color):
#         super().__init__(price)
#         self.color = color

#     def get_data(self):
#         return f"{super().get_data()}, Color {self.color}"


# # ===== Testing =====
# car1 = Car(500, "Blue")
# car2 = Car(700, "Black")

# print(car1.get_data())
# print(car2.get_data())



