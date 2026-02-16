import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -----------------------------
# Use your own data
# -----------------------------
data = {
    'Speed type I': {
        'KB-RRT': [100, 83.33, 100, 100, 100],
        'KB-RRT*': [91.66, 100, 91.66, 83.33, 100],
        'IKB-RRT': [88.88, 88.88, 88.88, 94.44, 88.88],
    },
    'Speed type II': {
        'KB-RRT': [100, 100, 83.33, 83.33, 100],
        'KB-RRT*': [100, 91.66, 75, 83.33, 91.66],
        'IKB-RRT': [88.33, 83.33, 88.88, 88.88, 88.88],
    },
    'Speed type III': {
        'KB-RRT': [100, 83.33, 83.33, 100, 83.33],
        'KB-RRT*': [75, 100, 83.33, 75, 83.33],
        'IKB-RRT': [88.88, 83.33, 77.77, 83.33, 72.22],
    }
}

# Convert to DataFrame
rows = []
for orchard, methods in data.items():
    for method, values in methods.items():
        for v in values:
            rows.append([orchard, method, v])
df = pd.DataFrame(rows, columns=['Orchard', 'Method', 'Path length (m)'])

# -----------------------------
# Plot
# -----------------------------
palette = {
    'KB-RRT': "#46c1e7",      # blue
    'KB-RRT*': "#f58616",     # orange
    'IKB-RRT': "#35e73e",     # green
}

plt.figure(figsize=(9, 5))
ax = sns.boxplot(
    data=df,
    x='Orchard',
    y='Path length (m)',
    hue='Method',
    palette=palette,
    width=0.6,
    fliersize=2,
    linewidth=1
)

# -----------------------------
# Adjust box, whiskers, caps, medians colors
# -----------------------------
for i, patch in enumerate(ax.patches):
    face_color = patch.get_facecolor()
    edge_color = tuple([c * 0.6 for c in face_color[:3]] + [1])  # darker edge
    patch.set_edgecolor(edge_color)
    patch.set_linewidth(1.5)

# Whiskers, caps, medians
lines = ax.lines
num_boxes = len(df['Method'].unique()) * len(df['Orchard'].unique())
for i in range(num_boxes):
    whisker_low = lines[i*6 + 0]
    whisker_high = lines[i*6 + 1]
    cap_low = lines[i*6 + 2]
    cap_high = lines[i*6 + 3]
    median = lines[i*6 + 4]

    face_color = ax.patches[i].get_facecolor()
    edge_color = tuple([c * 0.6 for c in face_color[:3]] + [1])

    whisker_low.set_color(edge_color)
    whisker_high.set_color(edge_color)
    cap_low.set_color(edge_color)
    cap_high.set_color(edge_color)
    median.set_color(edge_color)
    median.set_linewidth(1.5)

# -----------------------------
# Add average value line
# -----------------------------
avg_df = df.groupby(['Orchard', 'Method'])['Path length (m)'].mean().reset_index()

orchards = df['Orchard'].unique()
methods = ['KB-RRT', 'KB-RRT*', 'IKB-RRT']
offsets = [-0.25, 0, 0.25]

for i, orchard in enumerate(orchards):
    subset = avg_df[avg_df['Orchard'] == orchard]
    avg_values = [subset[subset['Method'] == m]['Path length (m)'].values[0] for m in methods]
    x_positions = [i + o for o in offsets]
    plt.plot(x_positions, avg_values, color='red', linewidth=2, label='Average value' if i == 0 else "")

# -----------------------------
# Add vertical divider lines
# -----------------------------
for i in range(len(orchards) - 1):
    plt.axvline(x=i + 0.5, color='gray', linestyle='--', linewidth=1)

# -----------------------------
# Style adjustments
# -----------------------------
plt.legend(title='', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.title('Path length comparison across orchards', fontsize=13)
plt.tight_layout()
plt.show()
