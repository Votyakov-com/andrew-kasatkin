import numpy as np

array = np.array([1, 2, 3, 3, 4, 3, 3, 1, 3, 4, 7])
Dict = dict()

for item in array:
    if item not in Dict:
        Dict[int(item)] = 1
    if item in Dict:
        Dict[int(item)] += 1

max_value = -100000
right_key = 0
for k, v in Dict.items():
    if v > max_value:
        max_value = v
        right_key = k

print(f'Most frequent value is: {right_key}')
