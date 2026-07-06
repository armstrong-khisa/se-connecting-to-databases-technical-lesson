import sqlite3
import pandas as pd

conn = sqlite3.connect("data.sqlite")

cur = conn.cursor()

cur.execute("""SELECT name FROM sqlite_master WHERE type='table';""")

tables = cur.fetchall()

print("Tables in the database:")
for table in tables:
    print(table[0])

conn.close()