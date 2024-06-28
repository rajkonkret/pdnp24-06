# bazy danych - przechowywanie danych
# sql, nosql
import sqlite3

try:
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    print('Baza danych została podłaczona')

    # sql
    query = '''
    CREATE TABLE IF NOT EXISTS hardware (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL);
    '''

    c.execute(query)
    conn.commit()
except sqlite3.Error as e:
    print("Bład podczas podłaczania bazy danych", e)
finally:
    if conn:
        conn.close()
        print("Połączenie zostało zamknięte")
