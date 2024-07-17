class HeavenlyBody:
    """Родительский класс HeavenlyBody"""

    def __init__(self, name, age, temperature, radius):
        self._name = name
        self._age = age
        self._temperature = temperature
        self._radius = radius

    def display(self):
        return f'Name: {self._name}\n' + \
            f'Age: {self._age}\n' + \
            f'Temperature: {self._temperature}\n' + \
            f'Radius: {self._radius}'


class Planet(HeavenlyBody):
    """Дочерний класс Planet"""

    def __init__(self, name, age, temperature, radius, orbital_speed):
        super().__init__(name, age, temperature, radius)
        self._orbital_speed = orbital_speed

    def display(self):
        return f'Name: {self._name}\n' + \
            f'Age: {self._age}\n' + \
            f'Temperature: {self._temperature}\n' + \
            f'Radius: {self._radius}\n' + \
            f'Orbital speed: {self._orbital_speed}'


class Star(HeavenlyBody):
    """Дочерний класс Star"""

    def __init__(self, name, age, temperature, radius, constellation):
        super().__init__(name, age, temperature, radius)
        self._constellation = constellation

    def display(self):
        return f'Name: {self._name}\n' + \
            f'Age: {self._age}\n' + \
            f'Temperature: {self._temperature}\n' + \
            f'Radius: {self._radius}\n' + \
            f'Constellation: {self._constellation}'




planet1 = Planet('Земля', 4540, '16.92', 6371, '29.8')
star1 = Star('Полярная звезда', 60, '5500', 47, 'Малая Медведица')

print(Planet.__doc__, end='\n')
print(planet1.display())
print()
print(Star.__doc__, end='\n')
print(star1.display())
