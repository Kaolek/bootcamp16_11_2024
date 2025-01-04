import requests

url = 'http://numbersapi.com/random/year?json'

response = requests.get(url)
data = response.json()
print(data)
print(type(data))


print("Podaj odpowiedź na pytanie:\n", data['text'].replace(str(data['number']), ""))
odp = input()
if odp == str(data['number']):
    print("Prawidłowa odpowiedź")
else:
    print("Błąd")