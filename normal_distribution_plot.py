import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Example data (replace with your own data)
data = [9, 10, 11, 9, 12, 8, 10, 10, 8, 9, 11, 11, 9]

# Calculate mean and standard deviation
mean = np.mean(data)
std = np.std(data)

# Plot the histogram
plt.hist(data, bins=10, density=True, alpha=0.6, color='g')

# Plot the normal distribution curve
xmin, xmax = plt.xlim()  # Get the limits of the x-axis
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mean, std)
plt.plot(x, p, 'k', linewidth=2)

# Adding title and labels
plt.title('Histogram with Normal Distribution Curve')
plt.xlabel('Value')
plt.ylabel('Density')

# Show the plot
plt.show()
