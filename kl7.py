from abc import abstractmethod, ABC


class Ptak(ABC):  # dziedziczymy po ABC, klasa jest abstrakcyjna
    """
    Klasa opisująca ptaka w pythonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością", self.szybkosc)

    @abstractmethod  # metoda abstrakcyjna, dekorator
    def wydaj_odglos(self):
        pass


class Kura(Ptak):
    def __init__(self, gatunek):
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam.")

    def wydaj_odglos(self):
        print("Ko k ok ko ko ")

    def dziobanie(self):
        print("Idę sobie podziobać")


class Orzel(Ptak):

    def wydaj_odglos(self):
        print("Kierr kier kir")

    def polowanie(self):
        print("Lece na polowanie")


class Sowa(Ptak):
    """
    klasa Sowa
    """


# Po oznaczeniu klasy jako abstrakcyjna, nie można tworzyc obiektów tej klay (Ptak)
# TypeError: Can't instantiate abstract class Ptak without an implementation for abstract method 'wydaj_odglos'
# orzel = Ptak("Orzeł Bielik", 45)
# orzel.latam()  # Tu Orzeł Bielik Lecę z szybkością 45
# orzel.wydaj_odglos()
#
# kur1 = Ptak("Kura Domowa", 0)
# kur1.latam()  # Tu Kura Domowa Lecę z szybkością 0
# kur1.wydaj_odglos()

kur2 = Kura("Kura Domowa")
kur2.latam()  # Tu Kura Domowa Ja nie latam.
kur2.wydaj_odglos()  # Ko k ok ko ko

or2 = Orzel("Orzel Bielik", 55)
or2.wydaj_odglos()
or2.latam()
or2.polowanie()
kur2.dziobanie()
# Lece na polowanie
# Idę sobie podziobać
# sowa = Sowa("Sowa", 5)
# TypeError: Can't instantiate abstract class Sowa without an implementation for abstract method 'wydaj_odglos'
