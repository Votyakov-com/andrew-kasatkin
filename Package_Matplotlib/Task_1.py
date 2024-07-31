import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(6.6, 6))

x = np.array(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
y = np.array([25, 28, 30, 27, 22, 24, 26])

plt.yticks(np.sort(y), ['22°C', '24°C', '25°C', '26°C', '27°C', '28°C', '30°C'])
plt.xticks(rotation=330)

plt.title('Average weekday temperature\n', fontsize=15)

plt.grid(True)
plt.plot(x, y)
plt.show()
