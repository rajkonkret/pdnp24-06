# dziedziczenie
# przejecie cech innej klasy, nadpisanie, modyfikacja, rozszerzec

class Pojazd:
    def __init__(self, kolor):
        self.kolor = kolor

    def info(self):
        print("Kolor", self.kolor)


class Samochod(Pojazd):  # dziedziczy po klasie pojazd
    """
    Klasa Samochód
    """

    def __init__(self, kolor, marka=None):
        super().__init__(kolor)  # Musimy obowiązkowo wywołać konstruktor z klasy wyższej
        # super() - klasa wyzsza
        self.marka = marka

    def info(self):
        super().info()  # Możemy wywołac metode info() z klasy wyzszej
        print("Marka", self.marka)


poj = Pojazd("Srebrny")
poj.info()

car = Samochod("Czerwony")
car.info()
# Kolor Srebrny
# Kolor Czerwony
# Po zmianie metody info() w kalsie Samochod
# Kolor Srebrny
# Kolor Czerwony
# Marka None

car2 = Samochod("zielony", "Fiat")
car2.info()

# polimorfizm - wspolne cechy obiektów róznych klas
lista = [poj, car, car2]
for o in lista:
    o.info()
# Marka None
# Kolor zielony
# Marka Fiat
# Kolor Srebrny
# Kolor Czerwony
# Marka None
# Kolor zielony
# Marka Fiat
