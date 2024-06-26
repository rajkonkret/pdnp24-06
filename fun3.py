a = 10
b = 15


def dodaj():
    a = 7  # zmienne lokalne
    b = 9  # zasięg w obrębie tylko tej funkcji
    print(a + b)


def dodaj2():
    print(a + b)  # uzyje globalnych


def dodaj3():
    global a
    a = 9
    b = 11
    print(a + b)


print(f"Wartosć a z góry wynosi {a}")  # Wartosć a z góry wynosi 10
dodaj()  # 16
print(f"Wartosć a z góry wynosi {a}")  # Wartosć a z góry wynosi 10
dodaj2()  # 25
print(f"Wartosć a z góry wynosi {a}")  # Wartosć a z góry wynosi 10
dodaj3()  # 20
print(f"Wartosć a z góry wynosi {a}")  # Wartosć a z góry wynosi 9
dodaj()
print(f"Wartosć a z góry wynosi {a}")  # Wartosć a z góry wynosi 9
# Wartosć a z góry wynosi 10
# 16
# Wartosć a z góry wynosi 10
# 25
# Wartosć a z góry wynosi 10
# 20
# Wartosć a z góry wynosi 9
# 16
# Wartosć a z góry wynosi 9
