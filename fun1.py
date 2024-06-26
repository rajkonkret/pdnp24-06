# funkcje - wydzielony fragment kodu, można go wywołać w dowolnym momencie
# deklaracja funkcji musi byc wczesniej niż wywołanie
# w miejscu deklaracji funkcja się nie wykonuje
# żeby funkcja się wykonała trzeba ją wywołać

a = 6
b = 8


# deklaracja funkcji
# słowko def nazwa funkcji nawiasy ()
# PEP8 - wymaga by były dwie puste linie
def dodaj():
    print(a + b)


def dodaj2(a, b):  # funkcja posiada dwa argumenty a i b obowiązkowe
    print(a + b)


def odejmij(a, b, c=0):  # a,b - obowiązkowe, c posiada wartość domyslna
    print(a - b - c)


# wywołanie funkcji
# nazwa funkcji nawiasy()
dodaj()  # 14
# dodaj2()  # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
# przekazywanie po pozycji
dodaj2(5, 8)  # 13
odejmij(1, 2)  # c = 0
odejmij(1, 2, 3)  # c = 3
# przekazywanie argumentów po nazwie
odejmij(c=3, b=6, a=10)
odejmij(b=6, a=10)
# argumenty mieszane
odejmij(1, c=90, b=67)  # -156
# odejmij(a=1, c=90, 67)  # SyntaxError: positional argument follows keyword argument
print(dodaj())  # None
# 14
# None
# print(dodaj() + dodaj2(7,9))
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
