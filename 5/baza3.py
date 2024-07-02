# bazy danych - przechowywanie danych
# sql, nosql
# CRUD
# Działanie	Instrukcja SQL	HTTP	DDS
# Create	INSERT	PUT / POST	write
# Read (Retrieve)	SELECT	GET	read / take
# Update	UPDATE	POST / PUT / PATCH	write
# Delete (Destroy)	DELETE	DELETE	dispose
import sqlite3

try:
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    print('Baza danych została podłaczona')

    insert = '''
    INSERT INTO hardware (id,name,price) VALUES (1,'Apple',6999);
    '''
    # insert write
    # c.execute(insert)
    # conn.commit()

    # select - read
    select = """
    SELECT * FROM hardware;
    """

    for row in c.execute(select):
        print(row)  # (1, 'Apple', 6999.0)
    # update
    update = """
    UPDATE hardware SET price=8999 WHERE id=1;
    """
    # c.execute(update)
    # conn.commit()

    delete = """
    DELETE FROM hardware WHERE id=1;
    """
    c.execute(delete)
    conn.commit()

except sqlite3.Error as e:
    print("Bład podczas podłaczania bazy danych", e)
finally:
    if conn:
        conn.close()
        print("Połączenie zostało zamknięte")
