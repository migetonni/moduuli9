class Car:
    def __init__(self, register_number, max_speed):
        self.register_number = register_number
        self.odometer = 0
        self.speed = 0
        self.max_speed = max_speed

    def print_info(self):
        print(f"Rekkari{self.register_number}"
              f"Huippunopeus {self.max_speed}"
              f"matkamittari {self.odometer}"
              f" nopeus {self.speed}")
someCar = Car("ABC-123", 142)

someCar.print_info()