# klasa abstrakcyjna -
# klasa w której nie można zrobić obiektu
# metoda abstrakcyjna
from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa opisująca ptaka w pythonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością", self.szybkosc)


@abstractmethod  # metoda abstrakcujna
class Kura(Ptak):
    def __init__(self, gatunek):
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def wydaj_odglos(self):
        print("Ko ko ko ko")

    def dziobanie(self):
        print("Tu", self.gatunek, "Idę sobie podziobać")


class Orzeł(Ptak):
    """
    Klasa orzeł
    """

    def wydaj_odglos(self):
        print("Kier Kir Kier")

    def polowanie(self):
        print('Tu', self.gatunek, "Rozpoczynam polowanie")


#
# nie można tworzyć obiektu tej klasy - klasa abstrakcyjna

# or1 = Ptak("Orzeł", 45)
# or1.latam()
# kur1 = Ptak("Kura", 0)
# kur1.latam()

kur2 = Kura("Kura domowa")
kur2.latam()
or2 = Orzeł("Orzeł bielik", 50)
or2.latam()

or2.wydaj_odglos()
kur2.wydaj_odglos()

or2.polowanie()
kur2.dziobanie()
# Tu Orzeł bielik Rozpoczynam polowanie
# Tu Kura domowa Idę sobie podziobać

# polimorfizm - obioekty różnych klas mają wspólne cechy
# klasa abstrakcyjna mocniej je akcentuje
lista = [or2, kur2]
for i in lista:
    print(i.__class__.__name__, i.wydaj_odglos())
# Kura None