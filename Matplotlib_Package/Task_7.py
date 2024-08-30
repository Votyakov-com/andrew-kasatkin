import matplotlib.pyplot as plt
import numpy as np

Y_label = "Количество посещений"
X_label = "День"

fig, axes = plt.subplots(1, 2, figsize=(10, 5), sharey="col")

x = np.arange(0, 5)
y1 = np.array([50, 60, 70, 80, 90])
y2 = np.array([40, 55, 75, 85, 95])

ax1 = axes[0]
ax2 = axes[1]

ax1.set_title("Посещения сайта A")
ax2.set_title("Посещения сайта B")
ax1.set_ylabel(Y_label)
ax2.set_ylabel(Y_label)
ax1.set_xlabel(X_label)
ax2.set_xlabel(X_label)

ax1.plot(x, y1)
ax2.plot(x, y2)

plt.show()
