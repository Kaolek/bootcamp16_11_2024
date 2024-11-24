from datetime import date, timedelta, datetime

today = date.today()
print(today)  # 2024-11-24
print(type(today))  # <class 'datetime.date'>

time = datetime.now()
print(time)  #
print(type(time))

print("Godzina", time.hour)
print("Dzień", today.day)

formatted_date = datetime.now().strftime("%d/%m/%Y")
print("Dzisiejsza data", formatted_date)

formatted_time = datetime.now().strftime("%H:%M")
print("Aktualna godzina", formatted_time)
print("Aktualna godzina", formatted_time.removeprefix("0"))

tomorrow = today + timedelta(days=1)
print(tomorrow)
products = [
    {'sku': 1, 'exp_date': today, 'price': 100.00},
    {'sku': 2, 'exp_date': today, 'price': 200.00},
    {'sku': 3, 'exp_date': tomorrow, 'price': 250},
    {'sku': 4, 'exp_date': today, 'price': 50},
    {'sku': 5, 'exp_date': today, 'price': 500.00},
]

for product in products:
    print(product)
    print(product['exp_date'])

    if product['exp_date'] != today:
        continue
    product['price'] *= 0.7
    print(f"""
price for sku {product['sku']}
is now {product['price']}
""")