class Car:
    """
    Klasa opisująca samochód w pythonie
    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        #hermetyzacja - ustawienie pola jako prywatne
        self.__predkosc = predkosc = 0

    def gaz(self):
        self.__predkosc += 10

    def licznik(self):
        print(f"Prędkość wynosi {self.__predkosc} km/h")

    def hamuj(self):
        if self.__predkosc > 0:
            self.__predkosc -=10
            self.__zmien_bieg()
        else:
            self.__predkosc = 0
            print("Zatrzymałeś się")

    def __zmien_bieg(self):
        print("Zmiana biegu")


car = Car("Opel", 2024)
car.gaz()
car.gaz()
car.gaz()
car.gaz()
car.gaz()
# AttributeError: 'Car' object has no attribute '__predkosc'. Did you mean: '_Car__predkosc'?
# po oznaczeniu pola jako prywatne nie można odczytać tego pola
# print(car.__predkosc) # 50
car.licznik() # Prędkość wynosi 50 km/h
car.__predkosc = 0 # pole publiczne
car.licznik() # Prędkość wynosi 50 km/h
car.hamuj()
car.hamuj()
car.hamuj()
car.hamuj()
car.hamuj()
car.licznik() # Prędkość wynosi 0 km/h
#enakapsulacja - hermetyzujemy pola i dajemy metody ...
car.hamuj() # Zatrzymałeś się
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Prędkość wynosi 0 km/h
# Zatrzymałeś się