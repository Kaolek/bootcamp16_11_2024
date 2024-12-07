# funkcja, która oblicza średnią ocen
from day_2.typy_danych_2_lista import liczby


def srednia(name=None, *cyfry):  # dowolna ilość argumentów pozycyjnych
    print(cyfry)
    count = len(liczby)
    suma = 0
    sum_p = suma(cyfry)
    try:
        for c in cyfry:
            suma += c

        avg = suma / count
        avg_p = sum_p / count
    except Exception as e:
        print("Błąd", e)
    else:
        print(f"Średnia dla ucznia {name} wynosi {avg_p}")
    finally:
        print("Następne obliczenie")


srednia()  # () - krotka, tupla
srednia(1) # (1,)
srednia(1, 2, 3, 4) # (1, 2, 3, 4)
srednia(1, 2, 3, 4, 5, 6) # (1, 2, 3, 4, 5, 6)
srednia("a", 1, 2, 3, 4, 5, 6) # (1, 2, 3, 4, 5, 6)

