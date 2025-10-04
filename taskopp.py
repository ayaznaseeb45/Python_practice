class LivingBeing():
    def __init__(self, color, legs, eyes, can_speak):
        self.color = color
        self.legs = legs
        self.eyes = eyes
        self.can_speak = can_speak

    def show_info(self):
        print(f"color: {self.color}, legs {self.legs}, eyes: {self.eyes}, canSpeak {self.can_speak}")

# livig = LivingBeing("blue", 4 , "Brown" , True)
# print(livig.color)

class Human(LivingBeing):
    def __init__(self, color, legs, eyes, can_speak, name):
        super().__init__(color, legs, eyes, can_speak)
        self.name = name

    def introduce(self):
        print("hello my name is {self.name}")
        self.show_info()


# human1 = Human("blue", 4 , "Brown" , True, "Ayaz")
# print(human1.__dict__)

class Animal(LivingBeing):
    def __init__(self, color, legs, eyes, can_speak, species):
        super().__init__(color, legs, eyes, can_speak)
        self.species = species

    def sound(self):
        print(f"This is a {self.species}. It makes a sound!")
        self.show_info()


animal1 = Animal("blue", 4 , "Brown" , True, "Yes")

print(animal1.__dict__)
animal1.sound()