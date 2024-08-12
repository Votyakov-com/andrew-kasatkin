from abc import ABC, abstractmethod


class GeometricFigures(ABC):
    @abstractmethod
    def get_perimeter(self):
        raise NotImplementedError('Error! Wrong value.')


class Triangle(GeometricFigures):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_perimeter(self):
        return f'Perimeter is: {self.side1 + self.side2 + self.side3}\n'

    def __str__(self):
        return f"Triangle with sides: {self.side1},{self.side2},{self.side3}."


class Square(GeometricFigures):
    def __init__(self, side):
        self.side = side

    def get_perimeter(self):
        return f'Perimeter is: {self.side * 4}\n'

    def __str__(self):
        return f"Square with side: {self.side}."


class Rectangle(GeometricFigures):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def get_perimeter(self):
        return f'Perimeter is: {(self.side1 + self.side2) * 2}\n'

    def __str__(self):
        return f"Rectangle with sides: {self.side1},{self.side2}."


figures = [Triangle(1, 2, 3), Triangle(4, 5, 6),
           Square(10), Square(20),
           Rectangle(6, 7), Rectangle(7, 8)]

for figure in figures:
    print(figure, figure.get_perimeter())
