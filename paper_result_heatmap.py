import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Data from the table
moving_speeds = [0.03, 0.06, 0.09]
weed_densities = [6, 12, 18]

# Accuracy data (rows: moving speeds, columns: weed densities)
accuracy_data = np.array([
    [100.00, 96.67, 91.11],  # 0.03 m/s
    [96.67, 91.67, 86.67],   # 0.06 m/s
    [93.33, 83.33, 82.22]    # 0.09 m/s
])

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Create heatmap
sns.heatmap(accuracy_data, 
            annot=True,  # Show values in cells
            fmt='.2f',   # Format to 2 decimal places
            cmap='RdYlGn',  # Red-Yellow-Green colormap (green=high, red=low)
            cbar_kws={'label': 'Accuracy (%)'},
            xticklabels=weed_densities,
            yticklabels=moving_speeds,
            vmin=80,  # Minimum value for color scale
            vmax=100,  # Maximum value for color scale
            linewidths=0.5,
            linecolor='gray',
            ax=ax)

# Set labels and title
ax.set_xlabel('Weed Density (weeds/m²)', fontsize=12, fontweight='bold')
ax.set_ylabel('Moving Speed (m/s)', fontsize=12, fontweight='bold')
ax.set_title('Weed Detection Accuracy Heatmap', fontsize=14, fontweight='bold', pad=20)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()