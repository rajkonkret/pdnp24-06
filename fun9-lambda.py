# funkcja lambda - skrócony zapis funkcji
# zwraca wynik, ma domyślnie return
# funkcja anonimowa, mozliwość deklaracji w miejscu wykonania

def odejmij2(a, b):
    return a - b


odejmij = lambda a, b: a - b
print(odejmij2(8, 4))
print(odejmij(8, 4))

oblicz_vat = lambda cena, vat=23: cena * (100 + vat) / 100
print(oblicz_vat(1000))
print(oblicz_vat(1000, 7))

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))  # dziecko
print(wiek(10))  # nastolatek
print(wiek(17))  # nastolatek
print(wiek(18))  # dorosły
print(wiek(25))  # dorosły

lista = [1, 2, 3, 4, 5, 50, 67, 100, 200, 500]
#  wypisac elementy listy pomnożone przez 2

l = []
for i in lista:
    l.append(i * 2)
print(l)  # [2, 4, 6, 8, 10, 100, 134, 200, 400, 1000]

print([i * 2 for i in lista])  # [2, 4, 6, 8, 10, 100, 134, 200, 400, 1000]


def zmien(x):
    return x * 2


l2 = []
for i in lista:
    l2.append(zmien(i))
print(l2)  # [2, 4, 6, 8, 10, 100, 134, 200, 400, 1000]

# funkcje wyższego rzędu
# map() - bierze element, wykonuje na nim operacje zadaną funkcja
print(f"Sprawdzenie map(): {list(map(zmien, lista))}")  # Sprawdzenie map(): [2, 4, 6, 8, 10, 100, 134, 200, 400, 1000]
# Użycie funkcji lambda jako funkcja anonimowa, deklaracja w miejscu wykonania
print(
    f"Sprawdzenie map(): {list(map(lambda x: x * 2, lista))}")  # Sprawdzenie map(): [2, 4, 6, 8, 10, 100, 134, 200, 400, 1000]
print(
    f"Sprawdzenie map(): {list(map(lambda x: x * 4, lista))}")  # Sprawdzenie map(): [4, 8, 12, 16, 20, 200, 268, 400, 800, 2000]
print(
    f"Sprawdzenie map(): {list(map(lambda x: x * 411, lista))}")  # Sprawdzenie map(): [411, 822, 1233, 1644, 2055, 20550, 27537, 41100, 82200, 205500]

# filtrowanie danych
l3 = []
for i in lista:
    if i < 3:
        l3.append(i)
print(l3)  # [1, 2]
# filter() - bierze elementy kolekcji, zwraca spełniające warunek
print(f"Sprawdzenie filter(): {list(filter(lambda x: x < 3, lista))}")  # Sprawdzenie filter(): [1, 2]
# > 50
print(f"Sprawdzenie filter(): {list(filter(lambda x: x > 50, lista))}")  # Sprawdzenie filter(): [67, 100, 200, 500]
# x >3 i x < 79
print(
    f"Sprawdzenie filter(): {list(filter(lambda x: x > 3 and x < 79, lista))}")  # Sprawdzenie filter(): [4, 5, 50, 67]
print(
    f"Sprawdzenie filter(): {list(filter(lambda x: 3 < x < 79, lista))}")  # Sprawdzenie filter(): [4, 5, 50, 67]
