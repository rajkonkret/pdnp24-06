# REST API
# GET, POST, PUT/PATCH, DELETE  - metody http
import requests

url = 'http://api.open-notify.org/astros.json'

response = requests.get(url)
print(response)  # <Response [200]>

# 2xx ok
# 3xx przekierowania
# 4xx 404 - błedny adres, 400 Bad request
# 5xx - błedy wyenętrne serwera
print(response.text)  # odczyt jsona
response_data = response.json()  # zamiana na słownik
print(response_data)
# {'people': [{'craft': 'ISS', 'name': 'Oleg Kononenko'}, {'craft': 'ISS', 'name': 'Nikolai Chub'},
#             {'craft': 'ISS', 'name': 'Tracy Caldwell Dyson'}, {'craft': 'ISS', 'name': 'Matthew Dominick'},
#             {'craft': 'ISS', 'name': 'Michael Barratt'}, {'craft': 'ISS', 'name': 'Jeanette Epps'},
#             {'craft': 'ISS', 'name': 'Alexander Grebenkin'}, {'craft': 'ISS', 'name': 'Butch Wilmore'},
#             {'craft': 'ISS', 'name': 'Sunita Williams'}, {'craft': 'Tiangong', 'name': 'Li Guangsu'},
#             {'craft': 'Tiangong', 'name': 'Li Cong'}, {'craft': 'Tiangong', 'name': 'Ye Guangfu'}], 'number': 12,
#  'message': 'success'}
print(response_data['people'])
for i in response_data['people']:
    print(i)
    print(i['name'])
    # {'craft': 'ISS', 'name': 'Oleg Kononenko'}
    # {'craft': 'ISS', 'name': 'Nikolai Chub'}
    # {'craft': 'ISS', 'name': 'Tracy Caldwell Dyson'}
    # {'craft': 'ISS', 'name': 'Matthew Dominick'}
    # {'craft': 'ISS', 'name': 'Michael Barratt'}
    # {'craft': 'ISS', 'name': 'Jeanette Epps'}
    # {'craft': 'ISS', 'name': 'Alexander Grebenkin'}
    # {'craft': 'ISS', 'name': 'Butch Wilmore'}
    # {'craft': 'ISS', 'name': 'Sunita Williams'}
    # {'craft': 'Tiangong', 'name': 'Li Guangsu'}
    # {'craft': 'Tiangong', 'name': 'Li Cong'}
    # {'craft': 'Tiangong', 'name': 'Ye Guangfu'}

# {'craft': 'Tiangong', 'name': 'Ye Guangfu'}
# Ye Guangfu