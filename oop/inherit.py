class Car:  # parent class
    
    def __init__(self, userbrand, usermodel):  # constructor
        self.brand = userbrand
        self.model = usermodel
    
    def all_data(self):  # method
        return f"brand name is {self.brand} and model name is {self.model}"


class bike(Car):  # child class (inheritance)
    
    def __init__(self, userbrand, usermodel, color):  # constructor
        super().__init__(userbrand, usermodel)
        self.color = color
    
    def all_data(self):  # method overriding
        return f"{super().all_data()} and color is {self.color}"


# create object
bike1 = bike("xoxo", 1985, "black")

# call method
print(bike1.all_data())
