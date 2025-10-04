class Device:
    def __init__(self, brand, power):
        self.brand = brand
        self.__power = power

    def get_power(self):
        return self.__power

    def show_info(self):
        print(f"Brand: {self.brand}, Power: {self.get_power()}W")


class Phone(Device):
    def __init__(self, brand, power, camera):
        super().__init__(brand, power,)
        self.camera = camera

    def charge(self):
        print(f"{self.brand} phone is charging... Power: {self.get_power()}W and camera{self.camera}")


class Laptop(Device):
    def __init__(self, brand, power, ram):
        super().__init__(brand, power)
        self.ram = ram

    def charge(self):
        print(f"{self.brand} laptop is charging... Power: {self.get_power()}W")


phone1 = Phone("Samsung", 25, "108MP")
laptop1 = Laptop("HP", 65, "16GB")

phone1.charge()

laptop1.charge()
