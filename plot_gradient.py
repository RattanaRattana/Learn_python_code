import numpy as np
import matplotlib.pyplot as plt

# Define the function and its gradient (partial derivatives)
def func(x, y):
    return x**2 + y**2  # Objective function f(x, y) = x^2 + y^2

def grad_func(x, y):
    dx = 2 * x  # Partial derivative of f with respect to x
    dy = 2 * y  # Partial derivative of f with respect to y
    return dx, dy

# Gradient descent parameters
learning_rate = 0.1  # Step size
iterations = 30  # Number of steps
start_point = np.array([2, 2])  # Starting point (x0, y0)

# Store the history of points for visualization
path = [start_point]

# Perform gradient descent
current_point = start_point
for _ in range(iterations):
    dx, dy = grad_func(current_point[0], current_point[1])
    current_point = current_point - learning_rate * np.array([dx, dy])
    path.append(current_point)

# Convert path to numpy array for plotting
path = np.array(path)

# Create a grid of points for the surface plot
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = func(X, Y)

# Create the figure and axis for the 3D plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface . cmap : "coolwarm", "viridis"
surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7)

# Plot the gradient descent path
ax.plot(path[:, 0], path[:, 1], func(path[:, 0], path[:, 1]), color='r', marker='o', label='Gradient Descent Path')

# Add color bar
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)

# Labels and title
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_zlabel("Z axis")
ax.set_title("Gradient Descent Visualization")

# Show the plot
plt.show()
