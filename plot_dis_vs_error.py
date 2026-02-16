import numpy as np
import matplotlib.pyplot as plt

# Dense sampling like your data
x = np.arange(0, 4500, 25)  # Every 25 meters

# Base declining trend (70 to 10)
base_trend = 70 - (x/4500) * 60
base_trend_1 = 130 - (x/4500) * 60

# High-frequency oscillations (creates the jagged look)
high_freq_noise = np.sin(x/50)*8 + np.cos(x/80)*6 + np.sin(x/120)*4

# Random noise with larger amplitude
random_noise = np.random.uniform(-15, 15, len(x))

# Frequent sudden jumps (8% chance)
jump_mask = np.random.random(len(x)) < 0.08
jumps = np.where(jump_mask, np.random.uniform(-20, 20, len(x)), 0)

# Combine everything
y_data = base_trend + high_freq_noise + random_noise + jumps
y_data = np.maximum(0, y_data)  # Keep non-negative

y_data_1 = base_trend_1 + high_freq_noise + random_noise + jumps
y_data_1 = np.maximum(0, y_data_1)  # Keep non-negative

plt.figure(figsize=(12, 5))

# Different line styles and markers
#plt.plot(x, y_data, 'r*--', label='Lego-Loam', markersize=3, linewidth=0.5)    # Red stars, dashed
#plt.plot(x, y_data, 'bo:', label='LIO-SAM', markersize=2, linewidth=0.4)       # Blue circles, dotted  
#plt.plot(x, y_data, 'g^-.', label='Ours', markersize=2, linewidth=0.4)        # Green triangles, dash-dot

# Or more explicitly:
plt.plot(x, y_data, color='firebrick', marker='*', linestyle='-.', 
          markersize=5, linewidth=0.5, label='Lego-Loam')
plt.plot(x, y_data_1, color='lightseagreen', marker='*', linestyle=':', 
          markersize=5, linewidth=0.5, label='LIO-SAM')
# plt.plot(x, y_data, color='green', marker='^', linestyle='-.',
#          markersize=7, linewidth=2, label='Ours')

plt.legend()
plt.grid(True, alpha=0.3)
plt.show()