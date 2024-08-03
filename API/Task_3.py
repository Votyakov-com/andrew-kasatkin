from PIL import Image
from io import BytesIO
import requests

url = "https://api.waifu.im/search"
response = requests.get(url, headers={"Authorization": "YOUR_ACCESS_TOKEN"})
data = response.json()

print(data)
# Можно-ли как-то красиво вывести json файл как ключ-значение?
# Не получилось обратиться ни к одному атрибуту данных
print(data["images"])
