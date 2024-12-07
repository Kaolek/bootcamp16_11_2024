# zrobić funkcję restauracja
# zamów_pizze, zamów_napój
# w zależności od parametru mamy zwrócić jedną z tych funkcji

def restauracja(typ_zamowienia):
    print("Witamy w naszej restauracji")

    def zamow_pizze(skladniki="pieczarki"):
        print("zamówiono pizza, składniki:", skladniki)

    def zamow_napoj(nazwa="herbata"):
        print('zamów napoj', nazwa)

    if typ_zamowienia.casefold().strip() == 'pizza':
        return zamow_pizze
    else:
        return zamow_napoj # zwracamy adres funkcji


zamowienie_pizza = restauracja('pizza')
zamowienie_pizza() # zamówiono pizza, składniki: pieczarki
zamowienie_pizza("pieczarki, szynka") # zamówiono pizza, składniki: pieczarki, szynka

zamowienie_napoj = restauracja("napoj")
zamowienie_napoj() # zamów napoj herbata
zamowienie_napoj("cola")  # zamów napoj cola

zamowienie_pizza() # zamówiono pizza, składniki: pieczarki
