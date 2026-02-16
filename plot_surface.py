import numpy as np
import matplotlib.pyplot as plt

# Create a grid of x and y values
x = np.arange(-8, 8.5, 0.5)
y = np.arange(-8, 8.5, 0.5)
X, Y = np.meshgrid(x, y)

# Compute r and sinc function
R = np.sqrt(X**2 + Y**2) + np.finfo(float).eps  # Avoid division by zero
Z = np.sin(R) / R

# Create the figure and 3D axis
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface with a gradient color map
surf = ax.plot_surface(X, Y, Z, cmap='viridis')  # You can use other cmaps like 'jet', 'plasma', etc.

# Add a color bar for reference
fig.colorbar(surf)

# Set the view angle (elevation=30°, azimuth=30°, roll=0°)
ax.view_init(elev=32, azim=32, roll=0)

# Labels and title
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_zlabel("Z axis")
ax.set_title("3D Surface Plot with Gradient Colors")

# Show the plot
plt.show()
