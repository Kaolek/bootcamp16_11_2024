import tkinter as tk
from tkinter import messagebox
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import IntegrityError


# Tworzymy połączenie z bazą danych
engine = create_engine("sqlite:///biblioteka.db")
Base = declarative_base()


# Klasy książek i użytkowników
class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

Base.metadata.create_all(engine)

# Tworzymy sesję
Session = sessionmaker(bind=engine)
session = Session()

new_book = Book(title="Kordian", author="Juliusz Słowacki")
new_book2 = Book(title="Pan Tadeusz", author="Adam Mickiewicz")
new_book3 = Book(title="Lalka", author="Bolesław Prus")
new_book4 = Book(title="Potop", author="Henryk Sienkiewicz")
new_book5 = Book(title="Wesele", author="Stanisław Wyspiański")
new_book6 = Book(title="Kamizelka", author="Bolesław Prus")

session.add_all(
    [new_book, new_book2, new_book3, new_book4, new_book5, new_book6]
)
# session.commit()

# Funkcje do obsługi wypożyczeń i zwrotów
def add_user():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()

    if not first_name or not last_name:
        messagebox.showerror("Błąd", "Wszystkie pola muszą być wypełnione.")
        return

    try:
        user = User(first_name=first_name, last_name=last_name)
        session.add(user)
        session.commit()
        messagebox.showinfo("Sukces", "Użytkownik został dodany.")
    except IntegrityError:
        session.rollback()
        messagebox.showerror("Błąd", "Nie udało się dodać użytkownika.")


def rent_book():
    book_id = book_id_rent_entry.get()
    user_id = user_id_rent_entry.get()

    if not book_id or not user_id:
        messagebox.showerror("Błąd", "Wszystkie pola muszą być wypełnione.")
        return

    book = session.query(Book).filter_by(id=book_id).first()
    user = session.query(User).filter_by(user_id=user_id).first()

    if not book or not user:
        messagebox.showerror("Błąd", "Książka lub użytkownik nie istnieje.")
        return

    session.delete(book)  # Wypożyczenie książki (usunięcie z dostępnych)
    session.commit()
    messagebox.showinfo("Sukces",
                        f"Książka '{book.title}' została wypożyczona przez {user.first_name} {user.last_name}.")


def return_book():
    book_id = book_id_return_entry.get()

    if not book_id:
        messagebox.showerror("Błąd", "Pole ID książki nie może być puste.")
        return

    book = session.query(Book).filter_by(id=book_id).first()

    if book:
        messagebox.showerror("Błąd", "Książka już znajduje się w bibliotece.")
        return

    book = Book(id=book_id, title="Unknown", author="Unknown")  # Przywracamy książkę
    session.add(book)
    session.commit()
    messagebox.showinfo("Sukces", "Książka została zwrócona.")


# Tworzymy okno aplikacji
window = tk.Tk()
window.title("Biblioteka")

# Sekcja dodawania użytkownika
tk.Label(window, text="Imię:").grid(row=0, column=0)
first_name_entry = tk.Entry(window)
first_name_entry.grid(row=0, column=1)

tk.Label(window, text="Nazwisko:").grid(row=1, column=0)
last_name_entry = tk.Entry(window)
last_name_entry.grid(row=1, column=1)

add_user_button = tk.Button(window, text="Dodaj użytkownika", command=add_user)
add_user_button.grid(row=2, column=0, columnspan=2)

# Sekcja wypożyczania książek
tk.Label(window, text="ID książki do wypożyczenia:").grid(row=3, column=0)
book_id_rent_entry = tk.Entry(window)
book_id_rent_entry.grid(row=3, column=1)

tk.Label(window, text="ID użytkownika:").grid(row=4, column=0)
user_id_rent_entry = tk.Entry(window)
user_id_rent_entry.grid(row=4, column=1)

rent_book_button = tk.Button(window, text="Wypożycz książkę", command=rent_book)
rent_book_button.grid(row=5, column=0, columnspan=2)

# Sekcja zwracania książek
tk.Label(window, text="ID książki do zwrócenia:").grid(row=6, column=0)
book_id_return_entry = tk.Entry(window)
book_id_return_entry.grid(row=6, column=1)

return_book_button = tk.Button(window, text="Zwróć książkę", command=return_book)
return_book_button.grid(row=7, column=0, columnspan=2)

window.mainloop()