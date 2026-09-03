# user1 = Bank("ayaz", 1000)
# print(user1.name)
# # print(user1.__balance)
# print(user1.get_all_data())
# print("***************")

# user1.set_balance(500)

   
# class Animal:
#     def sound(self):
#         print("Animal speaking")

# class Dog(Animal):
#     def sound(self):
#         print("Barking")

# class Cat(Animal):
#     def sound(self):
#         print("Meow")



# x1 = Animal()
# x1.sound()
# x2 = Dog()
# x2.sound()


class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

class Cow:
    def sound(self):
        print("Moo")

animal =  [Dog(), Cat(), Cow() ]

for x in animal:
    x.sound()