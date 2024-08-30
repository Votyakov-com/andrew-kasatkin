import matplotlib.pyplot as plt
import numpy as np

x = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
y = np.array([22, 18, 9, 8, 7, 6])

plt.xlabel("Языки программирования")
plt.ylabel("Популярность")
plt.title("Популярность языков программирования")

plt.minorticks_on()
plt.grid(which="major", color="red", linewidth="0.5")
plt.grid(which="minor", color="black", linewidth="0.5")

plt.bar(x, y, color=["r", "k", "g", "b", "yellow", "cyan"])
plt.show()
