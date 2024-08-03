import requests

url = "https://www.weatherapi.com/"
payload = {
    "Date": "No",
    "Age": "34",
}
response = requests.get(url, json=payload)

"""
Почему не получается выводить так? 
for k,v in dict(response.headers):
    print(k,v)
"""

"""
Посмотрел в ответах решение. 
Откуда можно узнать, что оформлять запрос следует именно так (в плане наличия аргументов key и q)
f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
"""

"""
Также, из готового решения приходит только ошибка 403 
"""

print(response.headers)
