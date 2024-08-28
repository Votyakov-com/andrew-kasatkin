import requests

# Можно ли оформить данную программу тоже как отдельный сервер с вводом данных через браузер,
# или доступен только один локальный URL?
# Если да, то как можно оформить забор данных в return`e через HTML и в этом же return`e отправить?

url = "http://192.168.1.169:1234/api/convert-temperature"
payload = {"celsius": "20"}

response = requests.post(url, json=payload)
print(response.json())
