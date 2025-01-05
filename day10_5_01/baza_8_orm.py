# ORM - Mapowanie obiektowo - relacyjne, to nowoczesne podejście do zagadnienia współpracy z baza danych
# charakterystyczną cechą jest wykorzystywanie filozofii programowania obiektowego
# zamiana obiektów na tabele w bazie danych

# pip install sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


# klasy odwzorowujące tabele - encje
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"<User(name={self.name}, age={self.age}>"


# Tworzenie połączenia z baza danych
# echo=True - logowanie zdarzeń baz danych
engine = create_engine('sqlite:///mydatabase.db', echo=True)
Base.metadata.create_all(engine)  # Tworzy tabele w bazie danych

# utworzenie obiekty sesji za pomocą będziemy łączyć się z bazą danych
Session = sessionmaker(bind=engine)
session = Session()

new_user = User(name="Jan Kowalski", age=30)
session.add(new_user)
session.commit()
session.close()

users = session.query(User).all()
for user in users:
    print(user)
    print(f"Imię: {user.name} wiek: {user.age}")

result = session.execute(text("SELECT * FROM users"))
for row in result:
    print(row)

select = text()
result = session.execute(text("SELECT * FROM users")).scalars()
for row in result:
    print(row)
