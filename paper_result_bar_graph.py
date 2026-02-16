import matplotlib.pyplot as plt
import numpy as np

# Data from the table
weed_densities = ['6', '12', '18']

# Accuracy data for each moving speed
accuracy_003 = [100.00, 96.67, 91.11]  # 0.03 m/s
accuracy_006 = [96.67, 91.67, 86.67]   # 0.06 m/s
accuracy_009 = [93.33, 83.33, 82.22]   # 0.09 m/s

# Set up bar positions
x = np.arange(len(weed_densities))
width = 0.25  # Width of each bar

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Create bars for each moving speed
bars1 = ax.bar(x - width, accuracy_003, width, 
               label='0.03 m/s', color='#2E7D32', 
               edgecolor='black', linewidth=0.7)

bars2 = ax.bar(x, accuracy_006, width, 
               label='0.06 m/s', color='#F57C00', 
               edgecolor='black', linewidth=0.7)

bars3 = ax.bar(x + width, accuracy_009, width, 
               label='0.09 m/s', color='#C62828', 
               edgecolor='black', linewidth=0.7)

# Add value labels on top of bars
def add_value_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.2f}%',
                ha='center', va='bottom', fontsize=9)

add_value_labels(bars1)
add_value_labels(bars2)
add_value_labels(bars3)

# Customize the plot
ax.set_xlabel('Weed Density (weeds/m²)', fontsize=12, fontweight='bold')
ax.set_ylabel('Accuracy (%)', fontsize=12, fontweight='bold')
ax.set_title('Weed Detection Accuracy Comparison at Different Moving Speeds and Weed Densities', 
             fontsize=13, fontweight='bold', pad=20)

# Set x-axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(weed_densities)

# Set y-axis limits
ax.set_ylim(0, 110)

# Add legend
ax.legend(title='Moving Speed', fontsize=10, title_fontsize=11, loc='upper right')

# Add grid for y-axis only
ax.yaxis.grid(True, linestyle='--', alpha=0.6)
ax.set_axisbelow(True)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()