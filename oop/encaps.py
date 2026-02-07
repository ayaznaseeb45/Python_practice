# Parent class
class Vehicle:
    def __init__(self, brand, model):  # Constructor
        self.__brand = brand           # Encapsulation: private attribute
        self.__model = model           # Encapsulation: private attribute
        print(f"Vehicle created: {self.__brand}, {self.__model}")

    def get_details(self):
        # Abstraction: only show necessary info
        return f"Brand: {self.__brand}, Model: {self.__model}" 

    def __del__(self):  # Destructor
        print(f"Vehicle destroyed: {self.__brand}, {self.__model}")


# Child class of Vehicle
class Cycle(Vehicle):
    def __init__(self, brand, model, color):
        super().__init__(brand, model)
        self.__color = color           # Encapsulation: private attribute
        print(f"Cycle created: {brand}, {model}, Color: {self.__color}")

    # Polymorphism: overriding get_details
    def get_details(self):
        return f"{super().get_details()}, Color: {self.__color}"

    # Polymorphism: different implementation in different classes
    def fuel_type(self):
        return "None, human powered"

    def __del__(self):  # Destructor
        print(f"Cycle destroyed: Color: {self.__color}")
        super().__del__()  # Call parent destructor


# Child class of Cycle
class Car(Cycle):
    def __init__(self, brand, model, color):
        super().__init__(brand, model, color)
        print(f"Car created: {brand}, {model}, Color: {color}")

    # Polymorphism: same method name, different behavior
    def fuel_type(self):
        return "Petrol or Diesel"

    def __del__(self):  # Destructor
        print(f"Car destroyed: {self._Car__brand}")
        super().__del__()  # Call parent destructor


# Testing objects
print("=== Creating Car Object ===")
car1 = Car("Toyota", 2020, "Black")
print(car1.get_details())    # Shows brand, model, color
print(car1.fuel_type())      # Polymorphism: Car version

print("\n=== Creating Cycle Object ===")
cycle1 = Cycle("Hero", 2020, "Red")
print(cycle1.get_details())  # Shows brand, model, color
print(cycle1.fuel_type())    # Polymorphism: Cycle version

print("\n=== Deleting Objects ===")
del car1
del cycle1
