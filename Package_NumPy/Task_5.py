import numpy as np

arr = np.array([[1, 2, 3], [3, 7, 1], [4, 4, 2], [2, 4, 9]])
unique_values, counts = np.unique(arr, return_counts=True)

print(f'Total number of lowest value: {counts[0]}')
