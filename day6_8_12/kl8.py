#klasa abstrakcyjna -
# klasa w której nie można zrobić obiektu
# metoda abstrakcyjna
from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa opisująca ptaka w pythonie
    """

    def __int__(self, gatunek, szybkosc):
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


class Orzeł(Ptak):
    """
    Klasa orzeł
    """

    def wydaj_glos(self):
        print("Kier Kir Kier")


#
#nie można tworzyć obiektu tej klasy - klasa abstrakcyjna

#or1 = Ptak("Orzeł", 45)
#or1.latam()
#kur1 = Ptak("Kura", 0)
#kur1.latam()

kur2 = Kura("Kura domowa")
kur2.latam()
or2 = Orzeł("Orzeł bielik", 50)
or2.latam()

or2.wydaj_glos()
kur2.wydaj_odglos()
