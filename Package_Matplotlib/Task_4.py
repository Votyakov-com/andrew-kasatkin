import matplotlib.pyplot as plt
import numpy as np

fruits = np.array(['Apples', 'Pears', 'Bananas', 'Oranges', 'Peaches'])
quantity = np.array([100, 85, 70, 60, 45])

plt.xticks(np.arange(0, 105, 5))
plt.title('Information of sold fruits\n')

plt.barh(fruits, quantity, color=['green', 'khaki', 'yellow', 'orange', 'peachpuff'])
plt.show()
