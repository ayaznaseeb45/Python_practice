# oop 
class Car:
    
    def __init__(self, userbrand, usermodel):
        self.brand = userbrand
        self.model = usermodel
    
    def all_data(self):
        return f"brand name is {self.brand} and model name is {self.model}"

class bike(Car):
   
    def __init__(self,userbrand, usermodel, color):
        super().__init__(userbrand, usermodel)
        self.color = color
   
    def all_data(self):
        return f"{super().all_data()} color is {self.color}"
        

bike1 = bike("xoxo", 1985, "black")
print(bike1.all_data())