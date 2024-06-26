import json

# json = {"name" : "Radek"}
# obiekt typu klucz - wartość
# odpowiednikiem jsona w pythonie jest słownik

person_dict = {'name': 'Radek', 'age': 40, 'czy_pali': None}
# {"name": "Radek", "age": 40, "czy_pali": null}
print(type(person_dict))

with open('nasze_dane.json', 'w') as f:
    json.dump(person_dict, f)
# {"name": "Radek", "age": 40, "czy_pali": null}

# upiekszenie
with open('nasze_dane.json', 'w') as f:
    json.dump(person_dict, f, indent=4)
# {
#     "name": "Radek",
#     "age": 40,
#     "czy_pali": null
# }

# posortowane klucze
with open('nasze_dane.json', 'w') as f:
    json.dump(person_dict, f, indent=4, sort_keys=True)
# {
#     "age": 40,
#     "czy_pali": null,
#     "name": "Radek"
# }

with open('nasze_dane.json', 'r') as f:
    data = json.load(f)

print(data)  # {'age': 40, 'czy_pali': None, 'name': 'Radek'}
print(type(data))  # <class 'dict'>

# jak wypisac name
print(data['name'])
print(data.get('name'))

json_text = json.dumps(data)
print(type(json_text))  # <class 'str'>
print(json_text)  # {"age": 40, "czy_pali": null, "name": "Radek"}

dict_json = json.loads(json_text)
print(dict_json)  # {'age': 40, 'czy_pali': None, 'name': 'Radek'}
print(type(dict_json))  # <class 'dict'>
