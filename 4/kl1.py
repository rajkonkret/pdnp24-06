# klasa - szablon, przepis
# hermetyzacja, dziedziczenie, polimorfizm, abstrakcja
# wskazuje minimum tego co obiekt musi posiadac
# pola, funkcje
# pola - zmienne
# działąmy na obiektach kalsy
# obiekt klasa (instancja) element zbudowany wg przepisu
# definicja klasy - nic się nie wykona

class Human:
    """
    Klasa Human opisująca człowieka w pythonie
    """
    imie = ""
    wiek = None
    plec = "k"

    def powitanie(self):
        print('Nazywam się', self.imie)  # cz1.imie


print(Human.__doc__)  # Klasa Human opisująca człowieka w pythonie
print(print.__doc__)
#   sep
#     string inserted between values, default a space.
#   end
#     string appended after the last value, default a newline.
#   file
#     a file-like object (stream); defaults to the current sys.stdout.
#   flush
#     whether to forcibly flush the stream.
# cd 4 - wejscie do katologu 4
# pydoc -b
cz1 = Human()
print(cz1)  # <__main__.Human object at 0x00000212156E7A10>
print(cz1.imie)
print(cz1.plec)
print(cz1.wiek)
#
# k
# None
cz1.imie = "Zosia"
cz1.wiek = 19
print(cz1.imie)
print(cz1.plec)
print(cz1.wiek)
cz1.powitanie()  # Nazywam się Zosia

cz2 = Human()
cz2.imie = "Radek"
cz2.wiek = 56
cz2.plec = "m"

lista = [cz1, cz2]
for p in lista:
    p.powitanie()
# Nazywam się Zosia
# Nazywam się Zosia
# Nazywam się Radek
