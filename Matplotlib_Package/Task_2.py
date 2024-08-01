import matplotlib.pyplot as plt
import numpy as np

genre = np.array(["Rock", "Pop", "Hip-hop", "Electronic", "Classical"])
quantity = np.array([30, 20, 15, 10, 25])

plt.title("Music preferences", fontsize=15, fontweight=1000)
plt.pie(quantity, labels=genre)

plt.show()
