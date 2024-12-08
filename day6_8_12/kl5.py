# dziedziczenie
class Pojazd:
    def __init__(self, kolor):
        self.kolor = kolor

    def info(self):
        print(f"Kolor: {self.kolor}")

class Samochód(Pojazd):
    """
    Klasa Samochód dziedziczy po klasie Pojazd
    """

    def __init__(self, kolor, marka="Fiat"):
        super().__init__(kolor) # obowiązkowo musimy wywołać konstruktor z klasy wyższej super()
        self.marka = marka

    def info(self):
        super().info() # możemy wywołać metode z klasy super()
        print(f"Marka {self.marka}")

class Rower(Pojazd):
    """
    Klasa Rower
    """

poj = Pojazd("czerwony")
poj.info() # Kolor: czerwony

sam = Samochód("zielony")
sam.info() # Kolor: zielony
# po nadpisaniu __init__ i info()
# Kolor: zielony
# Marka Fiat

rower = Rower("Żółty")
rower.info() # Kolor: Żółty

lista = [poj, sam, rower]
print(lista)
# [<__main__.Pojazd object at 0x103186540>,
# <__main__.Samochód object at 0x1031866f0>,
# <__main__.Rower object at 0x103186720>]

# obiekty różnych klas
# mają wspólną metode info()
# polimorfizm - obiekty różnych klas traktowane jako jedej.
for i in lista:
    print(i.__class__.__name__)
    i.info()
# Pojazd
# Kolor: czerwony
# Samochód
# Kolor: zielony
# Marka Fiat
# Rower
# Kolor: Żółty
