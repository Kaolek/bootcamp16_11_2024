import sqlite3

try:
    sql_connection = sqlite3.connect("sqlite_python.db")
    cursor = sql_connection.cursor()
    print("Baza danych została podłączona")

    query = '''
    CREATE TABLE SqliteDB_developers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT FULL,
    email TEXT NOT NULL UNIQUE,
    joining_date DATETIME
    salary REAL NOT NULL
    );
    '''
    # cursor.execute(query) # wykonanie polecenia na bazie danych
    # sql_connection.commit() # utrwalenie danych

    # wczytanie skryptu sql jako tekst do wykonania na bazie danych
    with open("tables.sql", "r") as file:
        sql_script = file.read()

        # wykonanie skryptu na bazie danych
        cursor.executescript(sql_script)

except sqlite3.Error as e:
    print("Błąd bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza danych została zamknięta")