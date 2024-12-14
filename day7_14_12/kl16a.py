# rson:
# init__(self, first_name, last_name, id):
# lf.first_name = first_name
# lf.last_name = last_name
# lf.id = id
#
#
# n("Jan", "Kowalski", 1)
import pickle
from dataclasses import dataclass


@dataclass
class Person:
    first_name: str
    last_name: str
    id: int

    def greet(self):
        print(self.first_name)

if __name__ == '__main__':
    p1 = Person("Jan", "Kowalski", 1)
    print(p1)  # Person(first_name='Jan', last_name='Kowalski', id=1)
    p2 = Person("Maciej", "Nowak", 2)
    print(p2)  # Person(first_name='Maciej', last_name='Nowak', id=2)

    people = [p1, p2]
    print(people)

with open("dane.pickle", "wb") as stream:
    pickle.dump(people, stream)
