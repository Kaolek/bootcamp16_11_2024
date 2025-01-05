import psycopg2

# pip install psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="mydatabase",
    user="myuser",
    password="mypassword",
)

cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name TEXT, email TEXT);")
conn.commit()

cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", ("Jan", "jan@rajkonkret.pl"))
cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", ("Anna", "anna@rajkonkret.pl"))
conn.commit()

cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
