import matplotlib.pyplot as plt
import numpy as np
import time

np.random.seed(int(time.time()))

x=np.random.uniform(-2,2,200)
y=np.random.normal(-3,3,200)

plt.scatter(x,y,color='r')
plt.show()