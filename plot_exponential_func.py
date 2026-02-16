import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Create an array of x values
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

y0 = np.array([0, 1, 3, 6, 8, 10, 9, 7, 6, 5])

# Define a smooth ramp function to simulate a smooth elbow effect and reach the max of x
def smooth_step(x, a=10):
    return (1 / (1 + np.exp(-a * (x - 0.5)))) * x.max()  # Scale sigmoid to match the max value of x

# Define the new y1 using a scaled smooth step response
y1 = smooth_step(y0)

# Define y2 as before
y2 =  y0 * (1 - np.exp(-2 * y0))  # y = 2(1 - e^(-2x))

# Define a Butterworth low-pass filter
def butter_lowpass_filter(data, cutoff, fs, order=2):
    nyq = 0.5 * fs  # Nyquist frequency
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = filtfilt(b, a, data)
    return y

# Filter parameters
cutoff = 5  # Cutoff frequency
fs = 150  # Sampling frequency

# Apply the Butterworth low-pass filter to smooth out the vibrations in y1
y3 = butter_lowpass_filter(y0, cutoff, fs)

# Create the figure and axis
plt.figure(figsize=(8, 6))

# plot a normal version

plt.plot(x, y0, label='Normal', color='black', linewidth=2)

# Plot the smoothed version of y1
plt.plot(x, y1, label='Smoothed y1 (with elbow)', color='blue', linewidth=2)

# Plot y = 2(1 - e^(-2x))
plt.plot(x, y2, label='y = 2(1 - e^(-2x))', color='red', linestyle='--', linewidth=2)

# Plot the low-pass filtered version of y1
plt.plot(x, y3, label='Low-pass filtered y1', color='green', linestyle='-.', linewidth=2)

# Add titles and labels
plt.title('Graphs of Smoothed y1 (with elbow), y = 2(1 - e^(-2x)), and Low-pass Filtered y1', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)

# Add a grid
plt.grid(True)

# Add a legend
plt.legend()

# Show the plot
plt.show()
