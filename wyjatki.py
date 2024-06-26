# wyjątki
# print(5 / 0)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\pdnp24-06\3\wyjatki.py", line 1, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero

# rzucanie błedów
# raise ValueError("Błąd wartości")
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\pdnp24-06\3\wyjatki.py", line 10, in <module>
#     raise ValueError("Błąd wartości")
# ValueError: Błąd wartości
numer = 90
try:
    # print(numer / 0)
    # print(numer / "00")
    # print("A" + 9)
    # print(int("A"))
    # raise KeyError("Bład klucza")
    wynik = numer / 5
except ZeroDivisionError:
    print("Dzielenie przez zero")
except TypeError:
    print("Bład typu")
except ValueError:
    print("Bład wartości")
except Exception as e:
    print("Bład", e)
else:  # wykona się tylko, gdy nie ma błedu
    print("Wynik działania", wynik)
finally:  # wykona się zawsze
    print("Wykona się zawsze")

print("Dalsza cześć programu")
# Bład 'Bład klucza'
# Dalsza cześć programu
# Wynik działania 18.0
# Dalsza cześć programu
