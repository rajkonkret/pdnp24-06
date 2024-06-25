# słownik  - para klucz - wartosc
# klucze nie moga sie powtórzyc
# {'user':'Radek'}
# słownik jest odpowiednik jsona

# pusty słownik
dictionary = dict()
print(dictionary)  # {}
print(type(dictionary))  # <class 'dict'>

dictionary1 = {}
print(type(dictionary1))  # <class 'dict'>

# dodawanie elementów do słownika
dictionary['imie'] = "Radek"
print(dictionary)  # {'imie': 'Radek'}
dictionary['wiek'] = 37
print(dictionary)  # {'imie': 'Radek', 'wiek': 37}

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
# dict_keys(['imie', 'wiek'])
# dict_values(['Radek', 37])
# dict_items([('imie', 'Radek'), ('wiek', 37)])

# nadpisanie elementu
dictionary['imie'] = 'Tomek'
print(dictionary)  # {'imie': 'Tomek', 'wiek': 37}

# wypisanie elementu
print(dictionary['imie'])  # Tomek
# print(dictionary['name'])  # KeyError: 'name'
print(dictionary.get('name'))  # None
print(dictionary.get('name', 'default'))  # default

dictionary.update({'date': '12-12-2024'})
print(dictionary)  # {'imie': 'Tomek', 'wiek': 37, 'date': '12-12-2024'}

dict_small = {'x': 2}
dict_small.update([('y', 3), ('z', 4)])
print(dict_small)  # {'x': 2, 'y': 3, 'z': 4}

# input() - pobiera dane od uzytkownika
# tekst = input("Wpisz tekst")  # zwraca <class 'str'>
# print(type(tekst))
# print(tekst)

# napisac program słownik pol-ang
# zbior danych - slownik
# wyswietlic klucze
# pobrac słówko od uzytkownika
# wypisac tłumaczenie

# pol_ang = {'kot': 'cat', 'pies': 'dog', 'jabłko': 'apple'}
# print("słówka do przetłumaczenia", pol_ang.keys())
# tekst = input("Podaj słowko")
# print(pol_ang[tekst.lower().replace(" ", "")])
# strip() - usunięcie spacji i białych znaków

# aplikacja kalkulator
# pobrac liczby od użytkownika
# wypisac wynik obliczenia np.: dodawanie
a = input("Podaj pierwsza liczbę")  # str
b = input("Podaj drugą liczbę")
print(a + b)  # to byłaby konkatenacja
print(int(a) + float(b))  # zrzutowane na liczby i obliczenie matematyczne
