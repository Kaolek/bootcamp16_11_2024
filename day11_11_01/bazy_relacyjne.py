# relacje w bazie danych
# typy relacji

# jeden do jednego - Obydwie tabele mogą zawierać tylko jeden rekord po każdej stronie




# jeden do wielu - tabele klucza podstawowego zawiera tylko jeden rekord, dotyczy jednego, żadnego,
# wielu rekordów powiązanej tabeli

# wiele do wiele - każdy rekord obydwu tabel może odnosić się do dowolnej liczby rekordów


from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

engine = create_engine('sqlite:///adress_book.db', echo=True)
Base = declarative_base()

# encje - klasy odwzorowujące tabele w bazie danych
class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(String)
    addresses = relationship(
        'Address',
        back_populates='person',
        order_by='Address.email',
        cascade='all, delete-orphan'
    )

    def __repr__(self):
        return f"{self.name} (id={self.id}"


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    person_id = Column(ForeignKey('person.id'))
    person = relationship("Person", back_populates='addresses')

    def __repr__(self):
        return self.email

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

anakin = Person(name='Anakin', age='38')
anakin2 = Person(name='Anakin Anakin', age=38)
anakin2.addresses = [Address(email='anakin@wp.pl')]

obi = Person(name=' Obi Wan Kenobi', age=45)
obi.addresses = [
    Address(email='obi@explain.com'),
    Address(email="waaka@gmail.com")
]
chewee = Person(name=' Chewbacca', age=45)
obi.addresses = [
    Address(email='obi@explain.com'),
    Address(email="waaka@gmail.com")
]

session.add(anakin)
session.add(anakin2)
session.add(obi)

session.commit()

all_ = session.query(Person).all()
print(all_)


first = session.query(Person).first()
print(first)
print(type(first))

print(first.name, first.age)

obi_list = session.query(Person).filter(
    Person.name.like('Obi%')
).all()
print(obi_list)

# id, name, age, email
chwee_list = session.query(Person).filter(
    Person.name.like('Che%')
).all()
print(chewee)

for o in chwee_list:
    print(f"{o.id=}, {o.name=}, {o.age=}, {o.addresses}")