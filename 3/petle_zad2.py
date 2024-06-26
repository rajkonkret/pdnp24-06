dictionary = {'imie': 'Radek', 'nazwisko': "Kowalski"}
print(type(dictionary))  # <class 'dict'>

# wyswietla klucze
for i in dictionary:
    print(i)
# imie
# nazwisko

for k in dictionary.keys():
    print(k)
# imie
# nazwisko

# wyswietlamy wartości
for v in dictionary.values():
    print(v)
# Radek
# Kowalski

# wyświetlenie par (itemów)
for i in dictionary.items():
    print(i)
# ('imie', 'Radek')
# ('nazwisko', 'Kowalski')
for k, v in dictionary.items():
    print(k, "=>", v)
# imie => Radek
# nazwisko => Kowalski
# sep  domyslnie spacja
#         string inserted between values, default a space.
#       end  domyslnie \n
#         string appended after the last value, default a newline.
print("Radek", end="")
print('Tomek')  # RadekTomek, ale tutaj end="\n"
print("Następne")  # Następne
# RadekTomek
# Następne
for k, v in dictionary.items():
    print(k, v, sep="=>")
# imie=>Radek
# nazwisko=>Kowalski

dictionary_2 = {'name': 'imie', 'company': "Inne"}
print({value: key for key, value in dictionary_2.items()})
# {'imie': 'name', 'Inne': 'company'}

d = {}  # pusty słownik
for k, v in dictionary_2.items():
    d[v] = k
print(d)  # {'imie': 'name', 'Inne': 'company'}
