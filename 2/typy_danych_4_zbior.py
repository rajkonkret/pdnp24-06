# zbiór - set - przechowuje unikalne elementy
# nie zachowuje kolejnosci przy dodawaniu elementów
# nie posiada indeksu

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)  # set() - rzutowani na zbiór (set)
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}

# utworzenie pustego zbiór
zb2 = set()
print(zb2)  # set()
print(type(zb2))  # <class 'set'>

# dodanie elementów do zbioru
zbior.add(33)
zbior.add(18)
zbior.add(18)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55}

# usunięcie elemntu ze zbioru
zbior.remove(55)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22}

# pop()  - usunięcie pierwszego elementu
print(zbior.pop())  # 33
print(zbior)  # {66, 777, 11, 44, 18, 22}

zbior_copy = zbior.copy()  # kopia elementów zbiorów
print(zbior_copy)
print(id(zbior))  # 2086373220064
print(id(zbior_copy))  # 2086373222752

zbior_2 = {667, 11, 44, 18, 52, 62, 999, 999, 12.34}
print(zbior_2)  # {999, 11, 44, 12.34, 18, 52, 667, 62}
print(type(zbior_2))  # <class 'set'>

# suma zbiorów
print(zbior | zbior_2)  # {66, 999, 777, 11, 44, 12.34, 18, 52, 22, 667, 62}
print(zbior)  # {66, 777, 11, 44, 18, 22}
print(zbior_2)  # {999, 11, 44, 12.34, 18, 52, 667, 62}
print(zbior.union(zbior_2))  # {66, 999, 777, 11, 44, 12.34, 18, 52, 22, 667, 62}

# część wspólna
print(zbior & zbior_2)  # {18, 11, 44}
print(zbior.intersection(zbior_2))  # {18, 11, 44}

# różnica
print(zbior - zbior_2)  # {777, 66, 22}
print(zbior.difference(zbior_2))  # {777, 66, 22}
print(zbior_2.difference(zbior))  # {999, 12.34, 52, 667, 62}

# łaczy zbiory, zmienia zbior bazowy !!!
zbior.update(zbior_2)
print(zbior)  # {66, 999, 777, 11, 44, 12.34, 18, 52, 22, 667, 62}

lista = list(zbior_2)
print(type(lista))  # <class 'list'>
print(lista)  # [999, 11, 44, 12.34, 18, 52, 667, 62]

krotka = tuple(zbior)
print(krotka)  # (66, 999, 777, 11, 44, 12.34, 18, 52, 22, 667, 62)
