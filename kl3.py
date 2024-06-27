class Car:
    """
    Klasa opisująca samochód w pythonie
    """

    def __init__(self, model, year):
        """
        Konstruktor
        :param model:
        :param year:
        """

        self.model = model
        self.year = year
        # hermetezycja - zabezpieczanie pol przed dostępem poza klasą
        self.__predkosc = 0  # pole prywatne

    # enkapsulacja - wystawienie metod do zabezpieczonych pól
    def gaz(self):
        self.__predkosc += 10

    def licznik(self):
        print(f"Prędkość wynosi {self.__predkosc} km/h")

    def hamuj(self):
        self.__predkosc -= 10


car1 = Car("Tesla", 2024)
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
# print(car1.__predkosc)
car1.licznik()  # Prędkość wynosi 50 km/h
car1.__predkosc = 0
car1.licznik()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.licznik()
# Prędkość wynosi 50 km/h
# Prędkość wynosi 50 km/h
# Prędkość wynosi 0 km/h
