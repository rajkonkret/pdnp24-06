# pliki csv
# plik tekstowy, w którym dane są oddzielone znakiem podziału (tab, ,;)
# Kowalski,Jan,Kłodzko

import csv

filename = 'records.csv'
row = ['Radek', 'Coe', 2, '9.1']
fields = ['name', 'branch', 'year', 'cgpa']

dictionary = dict(zip(fields, row))
print(dictionary)  # {'name': 'Radek', 'branch': 'Coe', 'year': 2, 'cgpa': '9.1'}

with open(filename, 'w', newline='') as csv_f:
    csvwriter = csv.writer(csv_f)
    csvwriter.writerow(fields)
    csvwriter.writerow(row)

# zapisanie danych ze słownika
filename = 'records_dict.csv'
with open(filename, 'w', newline='') as f:
    csvwriter = csv.DictWriter(f, fieldnames=fields)
    csvwriter.writeheader()
    csvwriter.writerow(dictionary)

dict_list = [
    {'name': 'Radek', 'branch': 'Coe', 'year': 2, 'cgpa': '9.1'},
    {'name': 'tomek', 'branch': 'Cos', 'year': 3, 'cgpa': '.1'},
    {'name': 'Zenek', 'branch': 'Cot', 'year': 4, 'cgpa': '19.1'},
    {'name': 'Marek', 'branch': 'Col', 'year': 5, 'cgpa': '9.11'},
]

# zapisanie danych z listy słowników
filename = "records_list_dict.csv"
with open(filename, 'w', newline='') as f:
    csvwriter = csv.DictWriter(f, fieldnames=fields, delimiter=";")
    csvwriter.writeheader()
    csvwriter.writerows(dict_list)
# newline ='' - ominięcie problemu pustej linii
# delimiter=";" - wskazanie znaku rozdziału danych
