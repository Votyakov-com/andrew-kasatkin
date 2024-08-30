import matplotlib.pyplot as plt
import numpy as np

patterns = np.array(["|", "\\", "/", "+", "-", ".", "*", "x", "o", "O"])

for item in range(patterns.size):
    plt.bar(item, 3, color="white", edgecolor="black", hatch=patterns[item])

plt.show()
