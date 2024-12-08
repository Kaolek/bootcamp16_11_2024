class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja

    def przedstaw_sie(self):
        print(f"Cześć, jestem {self.imie} {self.nazwisko}")

    def oblicz_pensje(self):
        return self.pensja


# zrobić klase Manager, dziedzicząc po Pracowniku

class Manager(Pracownik):
    """
    Klasa Manager
    """

    def __init__(self, imie, nazwisko, pensja, premia):
        super().__init__(imie, nazwisko, pensja)
        self.premia = premia

    def oblicz_pensje(self):
        return self.pensja + self.premia


pracownik = Pracownik("Jan", "Kowalski", 5000)
pracownik.przedstaw_sie() # Cześć, jestem Jan Kowalski
wyn_prac = pracownik.oblicz_pensje()
print(f"Wynagrodzenie dla pracownika {pracownik.imie} {pracownik.nazwisko} {wyn_prac}")
# Wynagrodzenie dla pracownika Jan Kowalski 5000

manago = Manager("Anna", "Nowak", 10000, 5000)
manago.przedstaw_sie() # Cześć, jestem Anna Nowak
wyn_manago = manago.oblicz_pensje()
print(f"Wynagrodzenie dla menagera {manago.imie} {manago.nazwisko} {wyn_manago}")
# Wynagrodzenie dla menagera Anna Nowak 15000