# dziedziczenie diamentowe

class A:
    def method(self):
        print("Metoda z klasy A")


class B(A):
    def method(self):
        print("Metoda z klasy B")


class C(A):
    def method(self):
        print("Metoda z klasy C")


class D(B, C):
    """
    Klasa D dziedziczy po B i C a one dziedziczą z A
    """


d = D()
d.method()
print(D.__mro__)


# class E(A, D):
#     pass
# print(E.__mro__)

class F(D, A):
    pass


print(F.__mro__)
