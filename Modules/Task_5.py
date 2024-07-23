from random import randint as rnd
from random import choice as chc

array = list()
for _ in range(10):
    array.append(rnd(1, 100))

print(chc(array))
