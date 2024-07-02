import csv
import functools

fields = []
rows = []

# filename = 'records_dict.csv'
filename = '../4/records_list_dict.csv'

with open(filename, 'r') as file:
    dialect = csv.Sniffer().sniff(file.read(1024))
    print(dialect.delimiter)  # ;
    file.seek(0)  # powrót odcxzytu na początek pliku
    csvreader = csv.reader(file, delimiter=";")
    csvreader = csv.reader(file, delimiter=dialect.delimiter)
    print(csvreader)  # <_csv.reader object at 0x000001BE221B58A0>

    fields = next(csvreader)  # weź bieżący element, ustaw wskaźnik na nstępny
    for row in csvreader:  # wystartuje od drugiego elementu po pierwszy pobierze instrukcja next()
        rows.append(row)

print(rows)
print(fields)
# [['Radek', 'Coe', '2', '9.1'], ['tomek', 'Cos', '3', '.1'], ['Zenek', 'Cot', '4', '19.1'],
#  ['Marek', 'Col', '5', '9.11']]
# ['name', 'branch', 'year', 'cgpa']
