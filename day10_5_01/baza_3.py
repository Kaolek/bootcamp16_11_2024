import sqlite3

try:
    sql_connection = sqlite3.connect("sqlite_python.db")
    cursor = sql_connection.cursor()
    print("Baza danych została podłączona")

    insert = """
    INSERT INTO software (id, name, price) VALUES(1, 'Python', 100);
    """

    insert2 = """
        INSERT INTO software (id, name, price) VALUES(2, 'Java', 1000);
        """

    insert3 = """
        INSERT INTO software (id, name, price) VALUES(3, 'C++', 101);
        """

    # cursor.execute(insert)
    # cursor.execute(insert2)
    # cursor.execute(insert3)
    # sql_connection.commit()

    select = """
    SELECT * FROM software;
    """

    for row in cursor.execute(select):
        print(row)


except sqlite3.Error as e:
    print("Błąd bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza danych została zamknięta")