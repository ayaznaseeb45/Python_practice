

import sys

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.data = [0] * 1000000  # simulate memory usage
        print(f"Constructor: Vehicle {self.brand} {self.model} created")
        print(f"Memory used by object: {sys.getsizeof(self.data)} bytes\n")

    def __del__(self):
        print(f"Destructor: Vehicle {self.brand} {self.model} destroyed")
        print("Memory freed automatically by Python\n")


# Testing
print("=== Creating Vehicle objects ===")
v1 = Vehicle("Toyota", 2020)
v2 = Vehicle("Honda", 2021)

print("=== Deleting one Vehicle object ===")
del v1  # Destructor called, memory freed

print("=== Deleting remaining Vehicle object ===")
del v2  # Destructor called, memory freed

print("=== End of Program ===")
