import numpy as np

dim=int(input('Quantity of numbers for one side of magic square: '))
array=np.empty((dim,dim))

for r in range(dim):
    for c in range(dim):
        number=(input(f'Enter your number for: {r+1} row and {c+1} column: '))
        array[r][c]=int(number)
print()
print('Your square:')
print(array)
print()

rows = np.sum(array, axis=0)
columns = np.sum(array, axis=1)

first_diagonal = np.trace(array)
second_diagonal = np.trace(np.flip(array, axis=1))

if rows.all() == columns.any() and first_diagonal == second_diagonal:
    print("This square is magic!")
else:
    print("This square is not magic!")