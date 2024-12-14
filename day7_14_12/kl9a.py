# dziedziczenie diamentowe
class Animal:
    def speak(self):
        print("Animal speaks")


class Mammal(Animal):
    def speak(self):
        super().speak()
        print("Mammal sounds")


class Bird(Animal):
    def speak(self):
        super().speak()
        print("Bird sound")


class Bat(Mammal, Bird):
    pass


bat = Bat()
bat.speak()
print(Bat.__mro__)
