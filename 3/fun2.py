# funkcje zwracające wynik
# funkcja musi końćzyć sie komendą return
# pierwszy return wychodzi z funkcji

def dodaj(a, b):
    return a + b


def odejmij(a=0, b=0, c=0):
    return a - b - c


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


print(dodaj(4, 5))  # 9
print(dodaj(5, 2) + dodaj(9, 34))  # 50
wyn = dodaj(6, 9)
print('Wynik', wyn)  # Wynik 15
print(odejmij())
print(odejmij(1, 2))
print(odejmij(1))
print(odejmij(1, 2, 3))
print(odejmij(c=9))
print(oblicz_vat(1000))
print(oblicz_vat(1000, 8))
print(oblicz_vat(vat=15, cena=1000))
# 1230.0
# 1080.0
# 1150.0
zm = oblicz_vat(5000)
print(f"Cena z vat {zm}")  # Cena z vat 6150.0
if zm == 6150:
    print("OK")  # OK
