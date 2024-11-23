# instrukcje warunkowe
# instrukcje sterowania przepływem programu
# if - sterowana warunkiem
# if warunek:
#   komenda(blok) wykonany gdy warunek spełniony

odp = True
print(bool(odp))  # True
odp = False
# debug tryn do uruchomienia programu linijka po linijce i sprawdzanie parametrów
if odp:
    # po dwukropku wcięcie
    # 4 spacje
    print("Brawo")  # Brawo
    print("Brawo")  # Brawo
    print("Brawo")  # Brawo
    print("Brawo")  # Brawo
    print("Brawo")  # Brawo
    print("Brawo")  # Brawo

print("Dalsza część programu")

odp = "Radek"
if odp == "Radek":
    print("Radek")  # Radek
odp = "Tomek"
if odp == "Radek":
    print("Radek")
else:  # działanie domyślne, gdy warunek niespełniony
    print("Inny przypadek")  # Inny przypadek

if True:
    pass  # nic nie rób

print("Dalej")

podatek = 0.9
alert_system = ("email")
error = ("error")
lista_b = []
if alert_system == "console":
    print("Stało się coś strasznego")
elif alert_system == "email":
    print("system email")
    if error == "error":
        lista_b.append("krytyczny")
    elif error == "medium":
        lista_b.append("ostrzeżenie")
    else:
        lista_b.append("inny błąd")
else:
    print("Inny")
print("Lista błędów", lista_b)

alert_dict = {'console': "Coś poszło nie tak",
              'email': {'critical': 'Krytyczny', 'medium': "Ostrzeżenie"}}

if alert_system == 'console':
    print(alert_dict[alert_system])
    print(alert_dict.get(alert_system, "Nie ma takiego systemu"))
elif alert_system == "email":
    errors = alert_dict[alert_system]
    print(errors.get(error, "Nie ma takiego błędu dla systemu email"))
else:
    print("inny")