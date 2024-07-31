import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 50])
y = np.array([0, 150])

plt.ylabel('Ось y')
plt.xlabel('Ось x')
plt.title('Нарисуй линию')

plt.plot(x, y)
plt.show()
