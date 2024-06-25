# kolekcja
# lista - przechowuje wiele danych, różnego typu na raz
# zachowuje kolejność przy dodawaniu do listy

lista = []
print(lista)  # []
print(type(lista))  # <class 'list'>

pusta_lista = list()
print(pusta_lista)  # []
print(type(pusta_lista))  # <class 'list'>

# append() - dodanie elemntów do listy
lista.append("Radek")
lista.append("Monika")
lista.append("Joanna")
lista.append("Klaudia")
lista.append("Kasia")
lista.append("Michał")
print(lista)
# ['Radek', 'Monika', 'Joanna', 'Klaudia', 'Kasia', 'Michał']
#     0         1         2          3        4         5
#     -6        -5        -4         -3       -2        -1
print(lista[0])  # Radek
print(lista[2])  # Joanna
print(lista[3])  # Klaudia
print(lista[5])  # Michał
print(len(lista))  # 6, ostani indeks 5
# print(lista[6])  # IndexError: list index out of range
print(lista[-1])  # Michał

# wypisac fragment listy, slicowanie
print(lista[0:3])  # start:stop  ['Radek', 'Monika', 'Joanna'], indeks 012, z prawej otwarty
print(lista[:3])  # ['Radek', 'Monika', 'Joanna']
print(lista[2:])  # ['Joanna', 'Klaudia', 'Kasia', 'Michał'] ostatni zostanie wypisany
print(lista[2:5])  # ['Joanna', 'Klaudia', 'Kasia'] tutaj nie zostanie wypisany element o indeksie 5
print(lista[:])  # ['Radek', 'Monika', 'Joanna', 'Klaudia', 'Kasia', 'Michał']
print(lista[-2:0])  # []  [4:0]
print(lista[0:-2])  # [0:4]
print(lista[2:3])  # ['Joanna']
print(lista[2:10])  # ['Joanna', 'Klaudia', 'Kasia', 'Michał']
print(lista[10:20])  # []
print(lista[2:2])  # []
print(lista[0:4:2])  # start:stop:krok  # ['Radek', 'Joanna']
# krok oznacza, że kolejny element nie bedzie następny tylko wg sumy
# biezący + krok np.: 0 + 2(krok) = 2
lista_15 = list(range(15))  # 0..14
print(lista_15)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(lista_15[-10])  # 5

# nadpisanie elementu
lista[2] = "Mikołaj"
print(lista)  # ['Radek', 'Monika', 'Mikołaj', 'Klaudia', 'Kasia', 'Michał']

# rozszerzenie listy, wstawienie na wskazany indeks
lista.insert(1, "Joanna")
print(lista)  # ['Radek', 'Joanna', 'Monika', 'Mikołaj', 'Klaudia', 'Kasia', 'Michał']
print(len(lista))  # 7
lista.insert(11, "Patryk")
print(lista)  # ['Radek', 'Joanna', 'Monika', 'Mikołaj', 'Klaudia', 'Kasia', 'Michał', 'Patryk']

# sprawdzenie indeksu elementu
print(lista.index("Monika"))  # 2
indeks = lista.index("Monika")
print(indeks)  # 2

# usunięcie elemnentu
lista.remove("Patryk")
print(lista)  # ['Radek', 'Joanna', 'Monika', 'Mikołaj', 'Klaudia', 'Kasia', 'Michał']

# usnięci elementu po indeksie
# zewraca informację jaki element został usunięty
print(lista.pop(indeks))  # Monika
print(lista)  # ['Radek', 'Joanna', 'Mikołaj', 'Klaudia', 'Kasia', 'Michał']
print(lista.pop())  # Michał  - usunie ostatni
print(lista.pop(-2))  # Klaudia

a = 1
b = 3
a = b
print(a, b)  # 3 3
b = 7
print(a, b)  # 3 7

lista_2 = lista  # a = b
lista_copy = lista.copy()  # kopia elementów listy
print(lista_2, lista)
print(lista_copy)  # ['Radek', 'Joanna', 'Mikołaj', 'Kasia']
# ['Radek', 'Joanna', 'Mikołaj', 'Kasia'] ['Radek', 'Joanna', 'Mikołaj', 'Kasia']
lista.clear()  # usunięcie wszystkich elemntów z listy
print(lista_2, lista)  # [] []
print(lista_copy)  # ['Radek', 'Joanna', 'Mikołaj', 'Kasia']
print(id(lista))  # 2558176448896
print(id(lista_2))  # 2558176448896
print(id(lista_copy))  # 2558179280256

liczby = [54, 999, 34, 22, 12.34, 687]
print(liczby)
print(type(liczby))  # <class 'list'>

liczby.sort()
print(liczby)  # [12.34, 22, 34, 54, 687, 999]

liczby = [54, 999, 34, 22, 12.34, 687, "A"]
# liczby.sort()  # TypeError: '<' not supported between instances of 'str' and 'int'

lista_osob = ['radek', 'ola', 'agata', 'lena']
lista_osob.sort()
print(lista_osob)  # ['agata', 'lena', 'ola', 'radek']
lista_osob.sort(reverse=True)
print(lista_osob)  # ['radek', 'ola', 'lena', 'agata']
lista_osob.reverse()
print(lista_osob)  # ['agata', 'lena', 'ola', 'radek']

liczby[3] = 6666
print(liczby[0:3])  # [54, 999, 34]
print(liczby[-2])  # 687
print(liczby[-3:])  # [12.34, 687, 'A']
print(liczby)  # [54, 999, 34, 6666, 12.34, 687, 'A']

print(liczby.pop(2))  # 34

tekst = "Pyt hon."
lista1 = list(tekst)  # rozpakowanie sekwencji
print(lista1)  # ['P', 'y', 't', ' ', 'h', 'o', 'n', '.']

lista2 = [tekst]
print(lista2)  # ['Pyt hon.']

krotka = tuple(liczby)  # tuple() - rzutowanie na krotkę (tuplę)
print(type(krotka))  # <class 'tuple'>
print(krotka)  # (54, 999, 6666, 12.34, 687, 'A')
