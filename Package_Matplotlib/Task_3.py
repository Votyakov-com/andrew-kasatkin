import matplotlib.pyplot as plt
import numpy as np

matches = np.arange(1, 6)
goals = np.array([2, 3, 1, 4, 2])
dropped = np.array([1, 2, 0, 3, 1])

plt.title('Favourite team results\n', fontsize=12)
plt.xlabel('Matches', fontweight=1000, loc='right')
plt.ylabel('Goals of two teams', fontweight=1000, loc='top')

plt.bar(matches, goals, label='Goals', color='green')
plt.bar(matches, dropped, label='Dropped', color='red')
plt.legend()

plt.show()
