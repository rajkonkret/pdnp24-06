import pandas
# pip install pandas w terminalu

data = pandas.read_csv('../4/records_list_dict.csv', delimiter=";")
print(data)
# 0  Radek    Coe     2   9.10
# 1  tomek    Cos     3   0.10
# 2  Zenek    Cot     4  19.10
# 3  Marek    Col     5   9.11

print(data.columns)  # Index(['name', 'branch', 'year', 'cgpa'], dtype='object')
print(data.values)
# [['Radek' 'Coe' 2 9.1]
#  ['tomek' 'Cos' 3 0.1]
#  ['Zenek' 'Cot' 4 19.1]
#  ['Marek' 'Col' 5 9.11]]
print(data.items)
# <bound method DataFrame.items of     name branch  year   cgpa
# 0  Radek    Coe     2   9.10
# 1  tomek    Cos     3   0.10
# 2  Zenek    Cot     4  19.10
# 3  Marek    Col     5   9.11>
