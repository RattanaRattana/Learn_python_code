
import numpy as np
import math
import matplotlib.pyplot as plt
t =np.arange(21)
ts = 1
i = int(0)

list_i=[]
list_alpha=[]
while True:
    alpha = (30*math.sin((math.pi/15)*i+0.5))
    list_i.append(i)
    list_alpha.append(alpha)
    i += 0.01
    i = round(i,5)
    
    if i >= 0.20:
        break

plt.plot(list_i, list_alpha)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('My first graph!')
plt.show()