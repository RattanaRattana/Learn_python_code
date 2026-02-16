import numpy as np
import matplotlib.pyplot as plt

# Example PID velocity output (simulated here for demonstration)
# This might be your PID controller's output data
time = np.linspace(0, 10, 100)  # Time axis
velocity_output = np.array([0, 538, 21])  # Simulated velocity data

# Define the exponential smoothing function
def exponential_smoothing(data, alpha):
    smoothed_data = np.zeros_like(data)
    smoothed_data[0] = data[0]  # Set the first point
    for t in range(1, len(data)):
        smoothed_data[t] = alpha * data[t] + (1 - alpha) * smoothed_data[t - 1]
    return smoothed_data

# Smoothing factor (alpha), between 0 and 1. Smaller values lead to more smoothing
alpha = 0.9  # Adjust based on how much smoothing you want

# Apply exponential smoothing to the PID velocity output
smoothed_velocity_output = exponential_smoothing(velocity_output, alpha)

# Plotting the original and smoothed velocity output
plt.figure(figsize=(8, 6))

# Original PID velocity output
plt.plot(time[:len(velocity_output)], velocity_output, label='Original PID Velocity Output', color='blue', linewidth=2)

# Smoothed velocity output
plt.plot(time[:len(smoothed_velocity_output)], smoothed_velocity_output, label='Smoothed Velocity Output', color='green', linestyle='--', linewidth=2)

# Add titles and labels
plt.title('Original and Smoothed Velocity Output from PID', fontsize=14)
plt.xlabel('Time', fontsize=12)
plt.ylabel('Velocity', fontsize=12)

# Add grid and legend
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
