user = "Tomek"  # str
wiek = 39  # int
wersja = 3.900001  # float - liczba zmiennoprzecinkowa
print(type(wersja))  # <class 'float'>
liczba = 123456234345  # int
print(type(liczba))  # <class 'int'>

print("Witaj %s masz teraz %d lat." % (user, wiek))  # Witaj Tomek masz teraz 39 lat.
# TypeError: %d format: a real number is required, not str
# print("Witaj %d masz teraz %s lat." % (user, wiek))  #
# % s - string
# %d - digit

print("Witaj %(user)s, masz teraz %(wiek)d lat." % {'user': user, 'wiek': wiek})
# Witaj Tomek, masz teraz 39 lat.
print("Witaj %(user)s, masz teraz %(age)d lat." % {'user': user, 'age': wiek})
# Witaj Tomek, masz teraz 39 lat.

print(f"Witaj {user}, masz teraz {wiek} lat.")
print("Witaj {}, masz teraz {} lat.".format(user, wiek))
# f - f string - sformatowany string

# stosuje zaokrąglanie
print("Używamy wersji pythona %i" % 3)  # Używamy wersji pythona 3
print("Używamy wersji pythona %f" % 3.9)  # Używamy wersji pythona 3.900000
print("Używamy wersji pythona %.1f" % 3.9)  # Używamy wersji pythona 3.9
print("Używamy wersji pythona %.2f" % 3.9)  # Używamy wersji pythona 3.90
print("Używamy wersji pythona %.0f" % 3.9)  # Używamy wersji pythona 4
print("Używamy wersji pythona %.f" % 3.9)  # Używamy wersji pythona 4
print("Wynik = %.2f" % 3.876)  # Wynik = 3.88
x = 3.14
print("Zero miejsc po przecinki %.f" % x)  # Zero miejsc po przecinki 3
print("X się nie zmieniło", x)  # X się nie zmieniło 3.14

y = round(x)
print("y =", y)
print("x =", x)
# y = 3
# x = 3.14

x = 3.1415
print(round(x, 2))  # 3.14

print(f"Używamy wersji Pythona {wersja}")  # Używamy wersji Pythona 3.900001
print(f"Używamy wersji Pythona {wersja:.1f}")  # Używamy wersji Pythona 3.9
print(f"Używamy wersji Pythona {wersja:.2f}")  # Używamy wersji Pythona 3.90
print(f"Używamy wersji Pythona {wersja:.0f}")  # Używamy wersji Pythona 4

print(f'{user:>10}')  # "     Tomek"
print(f'{user:<20}')  # "Tomek               "
print(f'{user:^20}')  # "       Tomek        "

print(liczba)  # 123456234345
print(f"Nasza duża liczba {liczba:,}")  # Nasza duża liczba 123,456,234,345
print(f"Nasza duża liczba {liczba:,}".replace(",", "."))  # Nasza duża liczba 123.456.234.345
print(f"Nasza duża liczba {liczba:,}".replace(",", " "))  # Nasza duża liczba 123 456 234 345

liczba2 = 123_456_789_123
print(liczba2)  # 123456789123
print(type(liczba2))  # <class 'int'>
