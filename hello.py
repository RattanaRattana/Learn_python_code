import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])
# change 1 change 2 change3
plt.plot(xpoints, ypoints)
plt.show()
speed = [31,111,138,28,59,77,97]

x = np.var(speed)
print(x)
