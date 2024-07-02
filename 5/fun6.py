# funkcja obliczająca średnią
def liczby(name=None, *cyfry):
    print(cyfry)
    suma = 0
    count = len(cyfry)
    suma_p = sum(cyfry)
    try:
        for c in cyfry:
            suma += c

        avg = suma / count
    except Exception as e:
        print("Błąd", e)
    else:
        print(f"Średnia dla ucznia {name} wynosi {avg}")
    finally:
        print("Skończyłem obliczenia")


liczby()
liczby(1, 2)
liczby(1, 2, 2, 3)
liczby(1, 2, 2, 3, 4, 5)
# ("Radek",1,2,3,4,5) -> name - imie, cyfry - oceny: name, *cyfry
# po dodaniu zmiennej name
liczby("Radek", 1, 2, 3, 4, 5)  # Średnia dla ucznia Radek wynosi 3.0

# ()
# Błąd division by zero
# Skończyłem obliczenia
# (2,)
# Średnia dla ucznia 1 wynosi 2.0
# Skończyłem obliczenia
# (2, 2, 3)
# Średnia dla ucznia 1 wynosi 2.3333333333333335
# Skończyłem obliczenia
# (2, 2, 3, 4, 5)
# Średnia dla ucznia 1 wynosi 3.2
# Skończyłem obliczenia
# (1, 2, 3, 4, 5)
# Średnia dla ucznia Radek wynosi 3.0
# Skończyłem obliczenia