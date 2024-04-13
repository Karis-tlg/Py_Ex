import sqlite3

conn = sqlite3.connect('databases.db')

cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

with open('database.txt', 'w') as f:
    for table in tables:
        table_name = table[0]
        f.write(f"Table: {table_name}\n")
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        for row in rows:
            f.write(str(row) + '\n')
        f.write('\n')

conn.close()
