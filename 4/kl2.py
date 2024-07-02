class Human:
    """
    Klasa opisująca człowieka w pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec='k'):
        """
        Metoda inicjalizująca - konstruktor
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitanie(self):
        print('Nazywam się', self.imie)  # cz1.imie

    # wypisz_wzrost, wypisz_wiek
    def wypisz_wzrost(self):
        print(f"Mam {self.wzrost} cm wzrosrtu.")

    def wypisz_wiek(self):
        print(f"Mam {self.wiek} lat.")

    def ruszaj(self):
        if self.plec == "k":
            print("Ruszyłam w drogę")
        else:
            print("Ruszyłem w drogę")


# cz1 = Human()  # TypeError: Human.__init__() missing 3 required positional arguments: 'imie', 'wiek', and 'wzrost'
cz1 = Human("Zosia", 34, 170)
print(cz1.imie)
cz1.powitanie()
# Zosia
# Nazywam się Zosia
cz1.wypisz_wiek()
cz1.wypisz_wzrost()

cz2 = Human("Radek", 70, 190, "m")
cz2.powitanie()
cz2.wypisz_wzrost()
cz2.wypisz_wiek()
# Nazywam się Radek
# Mam 190 cm wzrosrtu.
# Mam 70 lat.
lista = [cz1, cz2]
for p in lista:
    p.ruszaj()
# Ruszyłam w drogę
# Ruszyłem w drogę
