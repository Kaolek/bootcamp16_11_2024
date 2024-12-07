# dekorator - funkcja opakowująca inną funkcję w dodatkową funkcjonalność
# przyjmuje jako argument funkcje
# wykorzystuje zasady funkcji wewnętrznej
def dekor(fun):
    def wew():
        print("Dekoruj")
        return fun()

    return wew

@dekor
def hej():
    print("Hej!!")

hej() # Hej!!