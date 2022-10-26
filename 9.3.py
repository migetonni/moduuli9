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

    def accelerate(self, speed_change):
        if 0 < self.speed + speed_change < self.max_speed:
            self.speed = self.speed + speed_change


    def kulje(self, hours):
        if self.odometer > -1:
            self.odometer = self.speed * hours



someCar = Car("ABC-123", 142)

someCar.accelerate(30)
someCar.accelerate(70)
someCar.accelerate(50)

someCar.print_info()
someCar.accelerate(-200)
someCar.print_info()

someCar.kulje(2)
someCar.print_info()