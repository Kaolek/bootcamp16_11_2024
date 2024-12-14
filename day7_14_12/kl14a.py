class Matematyka:

    @staticmethod
    def dodaj(a, b):
        return a + b

    @staticmethod
    def odejmij(a, b):
        return a - b


wynik = Matematyka.dodaj(5, 6)
print(wynik)  # 11
wynik = Matematyka.odejmij(65, 34)
print(wynik)  # 31


# klasa metodami statycznymi
# celcjusz na frenheit
# farenheit na celcjusz

class KalkulatorTemperatur:

    @staticmethod
    def celcius_to_farenheit(celcius):
        return celcius * 9 / 5 + 32

    @staticmethod
    def farenheit_to_celcius(farenheit):
        return (farenheit - 32) * 5 / 9


print(KalkulatorTemperatur.farenheit_to_celcius(100))  # 37.77777777777778
print(KalkulatorTemperatur.celcius_to_farenheit(2))  # 35.6
print(KalkulatorTemperatur.celcius_to_farenheit(37.7777777777777778))
assert 100.0 == KalkulatorTemperatur.celcius_to_farenheit(37.7777777777777778)