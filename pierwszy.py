import sys  # dodanie biblioteki

print()  # wypisz/wydrukuj
# ctrl alt l - formatowanie kodu
print("Nazywam sie Radek")
print('Nazywam się Radek')
# print('Nazywam sie Radek")
#   File "C:\Users\CSComarch\PycharmProjects\pdnp24-06\1\pierwszy.py", line 5
#     print('Nazywam sie Radek")
#           ^
# SyntaxError: unterminated string literal (detected at line 5)
# ctrl / automatyczny komentarz
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
# ctrl d - powielanie linii
# type() - sprawdzanie typów
print(type("Radek"))  # <class 'str'> - teksty
print("39")
print(type("39"))  # <class 'str'>
print(39)
print(type(39))  # <class 'int'> liczby całkowite
print(sys.int_info)
# sys.int_info(bits_per_digit=30,
#              sizeof_digit=4,
#              default_max_str_digits=4300,
#              str_digits_check_threshold=640)
# print("39" + 39)  # TypeError: can only concatenate str (not "int") to str
print(39 + 39)  # 78
print("39" + "39")  # 3939 łaczenie tekstów - konkatenacja
print(int("39") + 39)  # int() - rzutowanie, zamiana na int
print("39" + str(39))  # str() zamiana na tekst
print("8" + "8" + "8")
print(8 + 8 + 8)

print(5 * "4")  # 44444

# zmienna - pudełko na dane
# w jedej chwili przechowuje jedną daną
# typowanie dynamiczne - w każdej chwili możemy wrzucic do zmiennej inny typ danych
# snake_case
# nazwa powinna sugerowac co zmienna zawiera

name = "Radek"  # str
print(name)  # wypisanie wartości zmiennej
print(type(name))  # <class 'str'>

name = 56
print(name)
print(type(name))  # <class 'int'>
# print(name + "Kowalski")  3 TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(str(name) + "Kowalski")  # 56Kowalski

name: str = 90  # to nie jest deklaracja typu!!!
# to jest tylko podpowiedx co bys chciał
print(name)
print(type(name))

age = 48
print(age)
print(type(age))  # <class 'int'>
