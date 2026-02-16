import matplotlib.pyplot as plt
import numpy as np

# Data from the table
weed_densities = [6, 12, 18]

# Accuracy data for each moving speed
accuracy_003 = [100.00, 96.67, 91.11]  # 0.03 m/s
accuracy_006 = [96.67, 91.67, 86.67]   # 0.06 m/s
accuracy_009 = [93.33, 83.33, 82.22]   # 0.09 m/s

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot lines for each moving speed
ax.plot(weed_densities, accuracy_003, 
        marker='o', linewidth=2, markersize=8, 
        label='0.03 m/s', color='#2E7D32')

ax.plot(weed_densities, accuracy_006, 
        marker='s', linewidth=2, markersize=8, 
        label='0.06 m/s', color='#F57C00')

ax.plot(weed_densities, accuracy_009, 
        marker='^', linewidth=2, markersize=8, 
        label='0.09 m/s', color='#C62828')

# Customize the plot
ax.set_xlabel('Weed Density (weeds/m²)', fontsize=12, fontweight='bold')
ax.set_ylabel('Accuracy (%)', fontsize=12, fontweight='bold')
ax.set_title('Weed Detection Accuracy vs Weed Density at Different Moving Speeds', 
             fontsize=14, fontweight='bold', pad=20)

# Set axis limits and grid
ax.set_ylim(75, 105)
ax.set_xlim(4, 20)
ax.grid(True, linestyle='--', alpha=0.6)

# Add legend
ax.legend(title='Moving Speed', fontsize=10, title_fontsize=11, loc='best')

# Set x-axis ticks
ax.set_xticks(weed_densities)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()