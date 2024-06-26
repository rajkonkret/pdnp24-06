from datetime import date, datetime, timedelta

today = date.today()
print(today)  # 2024-06-26

time = datetime.now()
print('Aktualny czas', time)  # Aktualny czas 2024-06-26 14:35:15.375381
print(type(time))  # <class 'datetime.datetime'>

# tomorrow = today + 1  # TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
# days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomorrow = today + timedelta(days=1)
print(f"Jutro będzie {tomorrow}")  # Jutro będzie 2024-06-27

print(time.time())
print(today.day)

formatted_date = datetime.now().strftime("%d/%m/%Y")
print(formatted_date)  # 26/06/2024

formatted_time = datetime.now().strftime("%H:%M")
print(formatted_time)  # 14:43

# zadanie domowe - wyswietlic czas w postaci 12h

# zamiana stringa na obiekt typu datatime
data_object = datetime.strptime("26/06/2024", '%d/%m/%Y')
print(data_object)  # 2024-06-26 00:00:00
print(type(data_object))  # <class 'datetime.datetime'>

products = [
    {'sku': 1, 'exp_date': today, 'price': 100},
    {'sku': 2, 'exp_date': today, 'price': 50},
    {'sku': 3, 'exp_date': tomorrow, 'price': 200.0},
    {'sku': 4, 'exp_date': today, 'price': 55.55},
]
# print(products)
for p in products:
    # print(p)  # {'sku': 1, 'exp_date': datetime.date(2024, 6, 26), 'price': 100}
    if p['exp_date'] != today:
        continue
    p['price'] *= 0.8  # price = price * 0.8
    print(f"""Price for sku {p['sku']}
is now {p['price']}""")
