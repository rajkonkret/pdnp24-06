# bazy danych - przechowywanie danych
# sql, nosql
import sqlite3

try:
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    print('Baza danych została podłaczona')

except sqlite3.Error as e:
    print("Bład podczas podłaczania bazy danych")
finally:
    if conn:
        conn.close()
        print("Połączenie zostało zamknięte")
