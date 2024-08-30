import re

text = 'ул. Кутузовская, дом № 13, корпус 3, квартира 98'
numbers = re.findall(r'\d+', text)
print(numbers)
