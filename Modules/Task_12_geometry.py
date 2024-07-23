import math

def circle(radius=5):
    return f'Circle area: {radius ** 2 * math.pi}\n' + \
        f'Circumference of the circle: {radius * math.pi * 2} '

def triangle(side1=7, side2=2, side3=8):
    sides = [side1, side2, side3]
    value1 = min(sides)
    value2 = max(sides)
    sides.remove(value1)
    sides.remove(value2)
    value3 = sides[0]
    if (value1 + value3) - value2 <= 0:
        raise ValueError('Wrong data!')
    else:
        p = (side1 + side2 + side3) / 2
        return f'Triangle perimeter: {side1 + side2 + side3}\n' + \
            f'Area of the triangle: {math.sqrt(p * (p - side1) * (p - side2) * (p - side3))} '

def square(side=15):
    return f'Area of square: {side ** 2}\n' + \
        f'Square perimeter: {side * 4}'

