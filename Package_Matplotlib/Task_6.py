import matplotlib.pyplot as plt
import numpy as np

x = np.array([10.0, 20.0, 30.0])
y1 = np.array([20, 40, 10])
y2 = np.array([40, 10, 30])

plt.ylabel('Ось y')
plt.xlabel('Ось x')
plt.title('Нарисуй график')

plt.plot(x, y1, label='Линия 1')
plt.plot(x, y2, label='Линия 2')
plt.legend()

plt.show()
