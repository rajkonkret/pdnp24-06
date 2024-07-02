import requests

url = 'http://api.nbp.pl/api/exchangerates/rates/A/USD/'
response = requests.get(url)
print(response)  # <Response [200]>

# 2xx ok
# 3xx przekierowania
# 4xx 404 - błedny adres, 400 Bad request
# 5xx - błedy wyenętrne serwera
print(response.text)  # odczyt jsona
response_data = response.json()  # zamiana na słownik
print(response_data)
# {'table': 'A', 'code': ''currency': 'dolar amerykański', USD',
#  'rates': [{'no': '125/A/NBP/2024', 'effectiveDate': '2024-06-28', 'mid': 4.032}]}
# currency, code , mid
print(response_data['currency'])
print(response_data['code'])
# dolar amerykański
# USD
print(response_data['rates'])
# [{'no': '125/A/NBP/2024', 'effectiveDate': '2024-06-28', 'mid': 4.032}]
print(response_data['rates'][0])  # {'no': '125/A/NBP/2024', 'effectiveDate': '2024-06-28', 'mid': 4.032}
print(response_data['rates'][0]['mid'])  # 4.032
