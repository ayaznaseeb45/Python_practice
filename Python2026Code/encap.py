
class Bank:
    def __init__(self, name , balance):
        self.name = name
        self.__balance = balance #this is private variable 

    def set_balance(self, amount):
        if amount >=0:
            self.__balance += amount
            print(f"Blance {self.__balance} has been updated in your account!")
        else:
            print("invalid amount")

    def get_all_data(self):
        return f"name of user is {self.name} and its account balnce is {self.__balance}"


user1 = Bank("ayaz", 1000)
print(user1.name)
# print(user1.__balance)
print(user1.get_all_data())
print("***************")

user1.set_balance(500)
