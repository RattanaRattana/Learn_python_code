import numpy as np
import matplotlib.pyplot as plt

# Parameters
h = 0.2
x_end = 1.0  # Plot up to x=1
steps = int(x_end / h) + 1

# Initialize arrays
x_vals = np.linspace(0, x_end, steps)
y_exact = np.exp(x_vals)

# Euler method initialization
y_euler = np.zeros(steps)
y_euler[0] = 1  # initial condition

# Euler method iteration
for i in range(steps - 1):
    y_euler[i + 1] = y_euler[i] + h * y_euler[i]

# Plotting
plt.plot(x_vals, y_exact, label='Exact solution $y=e^x$', color='blue')
plt.plot(x_vals, y_euler, label='Euler approximation', color='red', linestyle='--', marker='o')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Exact solution vs Euler method for $y\' = y$, $y(0) = 1$')
plt.legend()
plt.grid(True)
plt.show()
