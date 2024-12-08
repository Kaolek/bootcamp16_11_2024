# napisać klase Dom
#  ma posiadać pola prywatne, kolor, liczba okien, metraż
#  dodać metody do odczytu tych pól

class Dom:
    """
    Klasa opisująca dom w pythonie
    """

    def __init__(self, kolor, liczba_okien, metraz):
        self.__kolor = kolor
        self.__liczba_okien = liczba_okien
        self.__metraz = metraz

    def kolor_domu(self):
        print(f"Dom ma kolor {self.__kolor}")

    def liczba_okien_domu(self):
        print(f"Dom ma {self.__liczba_okien} okien")

    def metraz_domu(self):
        print(f"Dom ma {self.__metraz} metrów")

    def zmien_okna(self):
        odp = int(input("Podaj liczbę okien"))
        self.__liczba_okien = odp

    def zmien_metraz(self):
        odp = int(input("Podaj nowy metraż"))
        self.__metraz = odp

    def zmien_kolor(self):
        odp = int(input("Podaj nowy kolor"))
        self.__kolor = odp
        self.kolor_domu()

    def farba(self):
        print("Zabrakło farby")

dom = Dom("niebieski", 6, 155)
dom.kolor_domu() # Dom ma kolor niebieski
dom.liczba_okien_domu() # Dom ma 6 okien
dom.metraz_domu() # Dom ma 155 metrów