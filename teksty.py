tekst = "Witaj Świecie"
print(tekst)  # Witaj Świecie
print(type(tekst))  # <class 'str'>

# teksty są niemutowalne
tekst.upper()
print(tekst)  # Witaj Świecie
""" Return a copy of the string converted to uppercase. """
print(tekst.upper())
tekst2 = tekst.upper()  # zapamiętujemy w zmiennej wynoik działania upper()
print(tekst2)  # WITAJ ŚWIECIE
print(tekst)  # Witaj Świecie Oryginał nie jest zmieniany

tekst3 = tekst.lower()
print(tekst3)  # witaj świecie

print(tekst.count("i"))  # 3
print(tekst.count("j", 0, 4))  # 0123 Wita -> 0,z prawej strony zbiór otwarty
# indeksy numerowane są od zera
# Witaj Świecie
# 0123456789
print(tekst.removesuffix("Świecie"))  # "Witaj "
print(tekst.removeprefix("Witaj"))  # " Świecie"

tekst4 = "witaj dobry Świecie"
print(tekst4.replace("dobry ", ""))  # witaj Świecie

print(tekst4[4])  # j po numerze indeksu

encoded_s = tekst.encode('utf-8')
print(encoded_s)  # b'Witaj \xc5\x9awiecie'
# \x - liczba zapisana w kodzie szesnastkowym
print(type(encoded_s))
print(encoded_s.decode('utf-8'))  # Witaj Świecie

imie = "Radek"
tekst_format = f"\tMam na imię {imie}\n i lubie pythona.\b"
print(tekst_format)
# "	  Mam na imię Radek
#  i lubie pythona"
# \t tabulator
# \n nowa linia
# \b backspace - kasowanie ostatniego znaku

starszy = "Witaj %s!"  # %s - oczekuje stringa
print(starszy % imie)  # Witaj Radek! - w miejsce %s wstawil wartosć zmiennej imie

print("Witaj {}!".format(imie))  # Witaj Radek!

# tekst wielolinijkowy
print("""Tekst
    wielolinijkowy
        tabulator
        """)
# "Tekst
#     wielolinijkowy
#         tabulator"
