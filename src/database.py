import sqlite3
import pandas as pd

conn=sqlite3.connect("data/books.db")
cursor=conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS books(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Title TEXT NOT NULL,
    Author TEXT NOT NULL,
    Genre TEXT NOT NULL,
    Pages INTEGER NOT NULL,
    Year INTEGER NOT NULL,
    Rating REAL NOT NULL
    )
""")
conn.commit()