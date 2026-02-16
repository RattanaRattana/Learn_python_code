import numpy as np
import matplotlib.pyplot as plt

# Define your x and y0 data
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y0 = np.array([0, 10, 5, 15, 4, 10, 6, 15, 10, 4])
# Exponential smoothing function
def exponential_smoothing(data, alpha):
    smoothed_data = np.zeros_like(data)
    smoothed_data[0] = data[0]  # Set the first point
    for t in range(1, len(data)):
        smoothed_data[t] = alpha * data[t] + (1 - alpha) * smoothed_data[t - 1]
    return smoothed_data

# Smoothing factor (alpha), adjust this between 0 and 1 for more or less smoothing
alpha = 0.5

# Apply exponential smoothing only to the first few points of y0 (for example, first 5 points)
y0_smooth_start = exponential_smoothing(y0[:1], alpha)

# Combine the smoothed start with the rest of the unsmoothed data
y0_smoothed = np.concatenate((y0_smooth_start, y0[1:]))

# Create the figure and axis
plt.figure(figsize=(8, 6))

# Plot the original y0 data
plt.plot(x, y0, label='Original y0 data', color='blue', linewidth=2)

# Plot the selectively smoothed version of y0
plt.plot(x, y0_smoothed, label='Smoothed y0 (starting points)', color='green', linestyle='--', linewidth=2)

# Add titles and labels
plt.title('Original and Selectively Smoothed y0 Data (Starting Points)', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y0', fontsize=12)

# Add a grid
plt.grid(True)

# Add a legend
plt.legend()

# Show the plot
plt.show()
