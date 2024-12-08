# klasa - szablon, wzór, przepis
# obiekt - zbudowany wg przepisu
# enkapsulacja, hermetyzacja, abstrakcja, dziedziczenie, polimorfizm
# pola, funkcje
# klasa musi być najpierw zdeklarowana
# obiekt uruchamia elementy klasy

class Human:
    """
    Klasa Human opisująca człowieka w pythonie
    """
    imie = ""
    wiek = None
    plec = "k"

    def powitanie(self): # self = cz2
        print(f"Nazywam się {self.imie}")

    # wypisz wiek()
    def wypisz_wiek(self):
        print(f"Mam {self.wiek} lat.")
print(Human.__doc__)  # Klasa Human opisująca człowieka w pythonie
print(print.__doc__)

cz1 = Human()  # tworzenie obiektu klas
print(cz1.imie)  #
print(cz1.wiek)  # None
print(cz1.plec)  # k

cz1.imie = "Radek"
cz1.plec = "m"
cz1.wiek = 78
print(cz1.imie)  # Radek
print(cz1.plec)  # m
print(cz1.wiek)  # 78


cz2 = Human()
cz2.imie = "Ania"
cz2.plec = "k"
cz2.wiek = 38
print(cz2.imie) # Ania
print(cz2.plec) # k
print(cz2.wiek) # 38

cz1.powitanie() # Nazywam się Radek
cz2.powitanie() # Nazywam się Ania

cz1.wypisz_wiek() # Mam 78 lat.
cz2.wypisz_wiek() #Mam 38 lat.