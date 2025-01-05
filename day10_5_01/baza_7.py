import sqlite3

try:
    sql_connection = sqlite3.connect("sqlite_python.db")
    sql_connection.row_factory = sqlite3.Row
    cursor = sql_connection.cursor()
    print("Baza danych została podłączona")

    table_data = 'hardware'

    select = f"SELECT * FROM {table_data};"

    cursor.execute(select)
    rows = cursor.fetchall()
    for row in rows:
        print(dict(row))

except sqlite3.Error as e:
    print("Błąd bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza danych została zamknięta")