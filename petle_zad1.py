# pętle - możliwosc wykonannia wielokrotnie tego samego zadania
# for - petla itreracyjna
import random

for i in range(5):  # 0..4
    print(i)

for i in range(10):
    pass  # nic nie rób

for _ in range(10):  # _ niema zmienna
    pass
    print("Test")
    print(_)
# Test
# 0
# Test
# 1
# Test
# 2
# Test
# 3
# Test
# 4
# Test
# 5
# Test
# 6
# Test
# 7
# Test
# 8
# Test
# 9
for i in range(20):
    print(i * 2)

# lotto z petla
lista_kule = list(range(1, 50))  # range(1,50) od 1 do 49
lista_wylosowane = []
for i in range(6):
    wyn = random.choice(lista_kule)
    lista_kule.remove(wyn)
    lista_wylosowane.append(wyn)

print(lista_wylosowane)  # [16, 15, 26, 24, 8, 23]

for i in range(10):
    if i % 2 == 0:  # modulo, reszta z dzielenia
        print(i, "parzysta")

lista3 = [j for j in range(20) if j % 2 == 0]  # wypisze parzyste do listy
print(lista3)

for c in lista_wylosowane:
    if c > 10:
        print("większe od 10", c)
    print(c)

for i in range(0, 10, 2):  # start, stop, krok
    print(i)

for i in range(10, 0, -2):
    print(i)
# 10
# 8
# 6
# 4
# 2

for i in range(-10, 0):
    print(i)
# -10
# -9
# -8
# -7
# -6
# -5
# -4
# -3
# -2
# -1

for c in lista3:
    if c == 2:
        c += 1  # c= c +1
    print(c)
# spam += 1    spam = spam + 1
# spam -= 1    spam = spam - 1
# spam *= 1    spam = spam * 1
# spam /= 1    spam = spam / 1
# spam %= 1    spam = spam % 1

imiona = ['Radek', 'Tomek', 'Zenek', 'Ania']
print(imiona)  # ['Radek', 'Tomek', 'Zenek', 'Ania']
print(type(imiona))  # <class 'list'>

for p in imiona:
    print(p)
# Radek
# Tomek
# Zenek
# Ania

# wyswietlic z tej listy w postaci: 0 Radek
for p in imiona:
    print(imiona.index(p), p)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania

for i in range(len(imiona)):  # range(4) 0 do 3
    print(i, imiona[i])
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania

# enumerate() - zwraca numer elemntu i element
for i in enumerate(imiona):
    print(i)
# (0, 'Radek')
# (1, 'Tomek')
# (2, 'Zenek')
# (3, 'Ania')
a, b = (3, 'Ania')
print(a, b)
for i, p in enumerate(imiona):
    print(i, p)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania
for i, p in enumerate(imiona, start=1):
    print(i, p)
# 1 Radek
# 2 Tomek
# 3 Zenek
# 4 Ania

ludzie = ['Radek', 'Arek', 'Tomek', "Zenek"]
wiek = [44, 55, 66, 23]
# Radek 44
for i in ludzie:
    print(i, wiek[ludzie.index(i)])
# Radek 44
# Arek 55
# Tomek 66
# Zenek 23
ludzie = ['Radek', 'Arek', 'Tomek', "Zenek", "Ania"]
wiek = [44, 55, 66, 23]
# Radek 44
# for i in ludzie:
#     print(i, wiek[ludzie.index(i)])  # IndexError: list index out of range

# zip() - łaczy kolekcji
for i in zip(ludzie, wiek):
    print(i)
# ('Radek', 44)
# ('Arek', 55)
# ('Tomek', 66)
# ('Zenek', 23)
for l, w in zip(ludzie, wiek):
    print(l, w)
# Radek 44
# Arek 55
# Tomek 66
# Zenek 23

# 0 Radek 44
for i in enumerate(zip(ludzie, wiek)):
    print(i)
(0, ('Radek', 44))
(1, ('Arek', 55))
(2, ('Tomek', 66))
(3, ('Zenek', 23))
a, b = (3, ('Zenek', 23))
print(a, b)  # 3 ('Zenek', 23)
c, d = ('Zenek', 23)
print(c, d)  # Zenek 23
(a, (c, d)) = (0, ('Radek', 44))
for i, (o, w) in enumerate(zip(ludzie, wiek)):
    print(i, o, w)
# 0 Radek 44
# 1 Arek 55
# 2 Tomek 66
# 3 Zenek 23
