import numpy as np
import matplotlib.pyplot as plt

# Create a grid of x and y values
x = np.arange(-2, 2.1, 0.1)
y = np.arange(-2, 2.1, 0.1)
X, Y = np.meshgrid(x, y)

# Compute the function z
Z = X * np.exp(-X**2 - Y**2)

# Compute the gradient (partial derivatives)
DX, DY = np.gradient(Z, 0.1, 0.1)  # Step size should match meshgrid spacing

# Compute the magnitude of the gradient
M = np.sqrt(DX**2 + DY**2)  # Magnitude of the gradient

# Create the quiver plot with color gradient
plt.figure(figsize=(8, 6))
quiver = plt.quiver(X, Y, DX, DY, M, cmap='plasma')

# Add a color bar to indicate gradient magnitude
plt.colorbar(quiver, label="Gradient Magnitude")

# Labels and title
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Gradient Vector Field (Colored Quiver Plot)")

# Show the plot
plt.show()
