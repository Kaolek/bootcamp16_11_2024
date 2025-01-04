# url = https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
import requests
from datetime import datetime

url = "https://api.openweathermap.org/data/2.5/weather?q=Krakow&appid={API key}&&lang=p&format=jsonl&units=metric"

page = requests.get(url)
print(page)
print(page.text)

data = page.json()
print(data)

print(data['weather'][0]['description']) # scattered clouds
print(data['main']['temp']) # -2.05
print(data['main']['temp_min']) # -2.23
print(data['main']['temp_max'])
print(data['name']) # Krakow
print("---------")
sunrise = data['sys']['sunrise']
print("Wschód słońca", sunrise)
# timestamp - liczba sekund od epoki Unixa - 1 stycznia 1970
dt_object_sunrise = datetime.fromtimestamp(sunrise)
print("Wschód słońca", dt_object_sunrise)
print(5 * "-")
sunset = data['sys']['sunset']
dt_object_sunset = datetime.fromtimestamp(sunset)
print("Zachód słońca", sunset)
print("Zachód słońca", dt_object_sunset)