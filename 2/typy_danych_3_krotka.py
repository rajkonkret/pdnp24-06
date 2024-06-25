# krotka - kolekcja, niemutowalna
# pozwala efektywniej zarządzać pamięcią
# krotka jednoelementowa  - stała - zmienna

tupla = "Radek"
print(type(tupla))  # <class 'str'>

tupla_2 = ("Radek")
print(type(tupla_2))  # <class 'str'>

tupla3 = ("Radek",)
print(type(tupla3))  # <class 'tuple'>
tupla_4 = "Radek",
print(type(tupla_4))  # <class 'tuple'>
# PEP8 zaleca by tuple jednoelementową umieszczać w nawiasach

tupla_liczby = (43, 55, 22.34, 11, 200)
print(type(tupla_liczby))  # <class 'tuple'>
print(tupla_liczby)  # (43, 55, 22.34, 11, 200)

# tupla_liczby[2] = 123  # TypeError: 'tuple' object does not support item assignment
tupla_imiona = "Radek", "Monika", "Michał", "Joanna", "Klaudia", 'Kasia'

# del tupla_liczby[0]  # TypeError: 'tuple' object doesn't support item deletion
del tupla_liczby
# print(tupla_liczby)  # NameError: name 'tupla_liczby' is not defined

print(tupla_imiona.count("Radek"))  # występuje 1 raz
print(tupla_imiona.index("Monika"))  # Monika jest na indeksie 1

# Rozpakowanie tupli
tup = 1, 2
a, b = 1, 2
print(type((1, 2)))  # <class 'tuple'>
print(a, b)  # 1, 2
tup_1 = 1, 2, 3
# a, b = tup_1  # ValueError: too many values to unpack (expected 2)
print(a, b)

a, *b = tup_1  # * worek na pozostałe dane
print(a, b)  # 1 [2, 3]

print(tupla_imiona)  # ('Radek', 'Monika', 'Michał', 'Joanna', 'Klaudia', 'Kasia')
*name1, name2, name3 = tupla_imiona
print(name1, name2, name3)  # ['Radek', 'Monika', 'Michał', 'Joanna'] Klaudia Kasia

name1, name2, *name3 = tupla_imiona
print(name1, name2, name3)  # Radek Monika ['Michał', 'Joanna', 'Klaudia', 'Kasia']

name1, *name2, name3 = tupla_imiona
print(name1, name2, name3)  # Radek ['Monika', 'Michał', 'Joanna', 'Klaudia'] Kasia

lista = list(tupla_imiona)
print(lista)  # ['Radek', 'Monika', 'Michał', 'Joanna', 'Klaudia', 'Kasia']
print(type(lista))  # <class 'list'>

# sortowanie krotki zwraca liste
print(sorted(tupla_imiona))  # ['Joanna', 'Kasia', 'Klaudia', 'Michał', 'Monika', 'Radek']
