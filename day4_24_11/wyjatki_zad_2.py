def kalkulator():
    print("Witaj w prostym kalkulatorze!")
    print("Wpisz 'wyjscie' aby zakończyć program.")

    while True:
        operacja = input("Podaj operację (+, -, *, /): ")

        if operacja == 'wyjscie':
            print("Kończenie programu. Do widzenia!")
            break

        if operacja in ['+', '-', '*', '/']:
            try:
                liczba1 = float(input("Podaj pierwszą liczbę: "))
                liczba2 = float(input("Podaj drugą liczbę: "))

                if operacja == '+':
                    wynik = liczba1 + liczba2
                elif operacja == '-':
                    wynik = liczba1 - liczba2
                elif operacja == '*':
                    wynik = liczba1 * liczba2
                elif operacja == '/':
                    if liczba2 != 0:
                        wynik = liczba1 / liczba2
                    else:
                        print("Błąd: Dzielenie przez 0!")
                        continue

                print(f"Wynik: {wynik}")

            except ValueError:
                print("Błąd: Niepoprawna wartość! Podaj liczby.")
        else:
            print("Błąd: Niepoprawna operacja! Spróbuj ponownie.")


if __name__ == "__main__":
    kalkulator()

