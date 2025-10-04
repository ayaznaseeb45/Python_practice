class Animal:
    def __init__(self, name, legs):
        self.name = name
        self.__legs = legs

    def show_legs(self):
        return self.__legs

    def show_info(self):
        print(f"Animal: {self.name}, Legs: {self.show_legs}")


dog = Animal("Dog", 4)
dog.show_info()
