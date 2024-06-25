# instrukcje warunkowe
# instrukcje sterowania przepływem programu
# if
# w zależności od warunku wykonuje jedną lub drugą operację
odp = True
# odp = False
if odp:
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")

print('To jest dalsza częśc programu')

odp = "Radek"
if odp == "Radek":
    print('To jest Radek')  # To jest Radek

if odp == "Tomek":
    print("To jest Tomek")
else:  # w innym przypadku
    print("To nie jest Tomek!!!")  # To nie jest Tomek!!!

# podatek = 0
# zarobki = int(input("Podaj dochód"))
# if zarobki < 10000:
#     podatek = 0
# elif zarobki < 30000:
#     podatek = 0.2
# elif zarobki < 100000:
#     podatek = 0.4
# else:
#     podatek = 0.9
# print(f"Podatek wynosi {podatek * zarobki}")
# # 0.2 dla przedziału 10000 do 29999
# ctrl /
suma_zam = 150
if suma_zam > 100:
    rabacik = 25
else:
    rabacik = 0
print(f"Rabat wynosi {rabacik}")  # Rabat wynosi 25

rabat = 25 if suma_zam > 100 else 0
print(f"Rabat wynosi {rabat}")

# zasymulujemy system zbierania logów
# zmienne będa przechowywac dane, które przyszły z zewnętrznego systemu
# email, console, inny
# dla consule: "Stało sie coś strasznego"
# dla email: "System email"
# poziomy waznosci: error, medium, inny
# zapisac opis tych poziomów do listy - ale tylko gdy system email
lista_b = []
error = 'error'
alert_system = 'email'
if alert_system == 'console':
    print("Stało sie coś strasznego")
elif alert_system == 'email':
    print("System email")
    if error == 'error':
        lista_b.append("błąd krytyczny")
    elif error == 'medium':
        lista_b.append("Ostrzeżenie")
    else:
        lista_b.append("Inny")
else:
    print("Nie znam tego systemu")

print(lista_b)

# napisac test z...
# pytanie
# pobrac odpowiedź
# wyswietlic wynik
punkty = 0
odp = input("Podaj datę Chrztu Polski")
if odp == '966':
    print('Odpowiedź prawidłowa')
    # punkty = punkty + 1
    punkty += 1
else:
    print("Masz w książce na stronie 23")
print(punkty)
