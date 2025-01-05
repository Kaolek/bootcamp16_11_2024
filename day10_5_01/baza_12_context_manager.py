# context manager - narzędzie usprawniające prace np: z plikami
# with
# __enter__ wykonuje się przy uruchamianiu
# __exist__ wykonujde się przy wyjściu
import sqlite3


class SQLiteDBCContexManager:
    def __init__(self, db_name):
        """
        Metoda inicjalizująca, konsktruktor
        :param db_name:
        """
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):  # wykonuje się zawsze
        if self.conn:
            self.conn.commit()
            self.conn.close()


db_name = "my_data.db"
lista = []
with SQLiteDBCContexManager(db_name) as conn:
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT);")
    cursor.execute("INSERT INTO users (name) VALUES (?)", ("Karol",))
    cursor.execute("INSERT INTO users (name) VALUES (?)", ("Robert",))
    cursor.execute("INSERT INTO users (name) VALUES (?)", ("Tomek",))
    cursor.execute("INSERT INTO users (name) VALUES (?)", ("Alicja",))
    select = cursor.execute("SELECT * FROM users;")
    for i in select:
        print(i)
        lista.append(i)

print(lista)
