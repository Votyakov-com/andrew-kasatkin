import numpy as np

arr = np.array([[10, 15, 20], [5, 25, 15], [30, 10, 5]])
total_sales = np.sum(arr, axis=1)
print(total_sales)
