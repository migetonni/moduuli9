class Dog:
    counter = 0
    def __init__(self, dog_name, weight):
        self.name = dog_name
        self.weight = weight
        Dog.counter += 1
    def bark(self):
        if self.weight > 10:
            print(f"Wuuuu Wuf! Olen {self.name}")
        else:
            print(f"WufWUf! Olen {self.name}")



dog1 = Dog("Rekku", 8)


dog2 = Dog("Ruffe", 12)

dog1.bark(3)
dog2.bark(1)
print(Dog.counter)

#print("Koira1:", dog1.name, dog1.weight, "kg")
#print("Koira2:", dog2.name, dog2.weight, "kg")
