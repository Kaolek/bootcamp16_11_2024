# iteratory - pozwala w sposób sekwencyjny dostep do danych
# oszczedza zużycie pamięci
# zapamiętuje gdzie zakończyliśmy

lista = [1, 2, 3, 4, 5]
print(lista)
for i in lista:
    print(i)

iterator = iter(lista)
print(iterator)  # <list_iterator object at 0x1051abee0>
print(type(iterator))  # <class 'list_iterator'>
# for i in iterator:
#     print(i)

print(next(iterator))  # 1
print("Zrób coś")  # Zrób coś
print("Dalej")  # Dalej
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))  # 5


# print(next(iterator)) # StopIteration, iterator wyczerpał dane

class Count:
    def __init__(self, low, high):
        """
        :param low: start licznika
        :param high: koniec licznika
        """
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
        return self.current - 1


print("--------")
counter = Count(1, 20)
print(next(counter))  # 1
