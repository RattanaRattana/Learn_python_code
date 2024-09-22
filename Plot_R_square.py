import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

x = np.array([1,5,6,8,11])
y = np.array([1,5,6,8,11])

plt.scatter(x,y)

slope, intercept, rvalue, pvalue, stderr = stats.linregress(x,y)

plt.plot(x,slope*x+intercept)

plt.annotate("y=%.3fx+%.3f\nR$^2$=%.3f\np=%.3f"%(slope,intercept,rvalue**2,pvalue),xy=(0.15,0.7),xycoords='figure fraction')

plt.show()