# zrobic klasę Dom
# metraz, kolor, liczba_okien
# pola mają byc prywatne
# wystawic metody do odczytu i zapisu tych pól
# dodac komentarz dokumentację
# stworzyć obiekty tej klasy
# wykorzystac ich funkcje
# wypisz_kolor, wypisz...
# zmien_kolor, zmien_...
class Dom:
    """
    Klsa opisująca dom w pythonie
    """

    def __init__(self, metraz, kolor, liczba_okien):
        """
        Metoda inicjalizujaca
        :param metraz:
        :param kolor:
        :param liczba_okien:
        """
        self.__metraz = metraz
        self.__kolor = kolor
        self.__liczba_okien = liczba_okien

    def mam_kolor(self):
        print(f"Mam kolor {self.__kolor}")

    def mam_metraz(self):
        print(f"Mam metraż {self.__metraz}")

    def mam_okna(self):
        print(f"Liczba okien {self.__liczba_okien}")

    def zmien_kolor(self):
        odp = input('Podaj nowy kolor')
        self.__kolor = odp
        self.mam_kolor()

    def zmien_metraz(self):
        odp = int(input('Podaj nowy metraż'))
        self.__metraz = odp
        self.mam_metraz()

    def zmien_okna(self):
        odp = int(input('Podaj ile okien'))
        self.__liczba_okien = odp
        self.mam_okna()


dom1 = Dom(200, "biały", 15)
dom1.mam_okna()
dom1.mam_metraz()
dom1.mam_kolor()
# Liczba okien 15
# Mam metraż 200
# Mam kolor biały
dom1.zmien_okna()  # Liczba okien 45
