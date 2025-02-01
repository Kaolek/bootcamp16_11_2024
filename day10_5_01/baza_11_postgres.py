import asyncio  # działania równoległe
import asyncpg



async def fetch_data():
    conn = await asyncpg.connect(
        user='37970432_dane',
        password='Radito_02',
        database='37970432_dane',
        host='serwer2348480.home.pl')

    try:
        rows = await conn.fetch('SELECT * FROM users;')
        for row in rows:
            print(row)

        # pojedynczy wiersz
        single_row = await conn.fetchrow("SELECT * FROM users WHERE id=$1;", 1)
        if single_row:
            print(f"Single Row -> ID: {single_row['id']}")
    finally:
        await conn.close()


asyncio.run(fetch_data())
