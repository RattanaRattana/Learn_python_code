import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Generate reference points (fixed)
reference_points = np.array([
    [0.0, 0.0],
    [1.0, 0.0],
    [1.0, 1.0],
    [0.0, 1.0]
])

# Generate initial source points (movable)
source_points = np.array([
    [0.7, -0.7],
    [1.5, -0.5],
    [1.5, 0.5],
    [0.5, 0.5]
])

# Function to find the closest points from source to reference
def find_closest_points(source, reference):
    closest_points = []
    for s in source:
        distances = np.linalg.norm(reference - s, axis=1)  # Compute distances
        closest_point = reference[np.argmin(distances)]  # Find the closest reference point
        closest_points.append(closest_point)
    return np.array(closest_points)

# Initialize plot
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1, 2)
ax.set_ylim(-1, 2)
ax.set_title("2D Point Cloud Alignment Animation")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")

# Plot reference cloud
ax.scatter(reference_points[:, 0], reference_points[:, 1], color='red', label='Reference Cloud', marker='o')

# Plot initial source cloud
sc_source = ax.scatter(source_points[:, 0], source_points[:, 1], color='blue', label='Source Cloud', marker='x')
ax.legend()
ax.grid()

# Animation function to update the source cloud in each frame
def update(frame):
    global source_points
    # Find closest points in reference for the current source points
    closest_points = find_closest_points(source_points, reference_points)
    
    # Calculate movement towards closest reference points
    for i in range(len(source_points)):
        # Move each source point towards its closest reference point
        source_points[i] += 0.1 * (closest_points[i] - source_points[i])  # Incrementally move towards closest reference
    # Update plot data for the source cloud
    sc_source.set_offsets(source_points)
    return sc_source,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=50, interval=100, blit=True)

plt.show()
