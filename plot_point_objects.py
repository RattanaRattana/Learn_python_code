import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

np.random.seed(0)  # For reproducibility

# Generate point clouds for static and dynamic obstacles
def generate_obstacle(center, size, n_points=30):
    return center + size * (np.random.rand(n_points, 3) - 0.5)

# Generate particle velocities
def generate_particles(points, speed=1.0):
    velocities = speed * (np.random.rand(len(points), 3) - 0.5)
    return velocities

# Create 3D plot canvas
fig = plt.figure(figsize=(16, 4))

### --- (a) Point objects
ax1 = fig.add_subplot(141, projection='3d')
static_pts = generate_obstacle(center=[0, 0, 3], size=2)
dynamic_pts = generate_obstacle(center=[1, 0, -2], size=2)

ax1.scatter(*static_pts.T, color='blue')
ax1.scatter(*dynamic_pts.T, color='blue')
ax1.text(0, 0, 4, 'static\nobstacle', backgroundcolor='lightgray')
ax1.text(1, 0, -2.5, 'dynamic\nobstacle', backgroundcolor='lightgray')
ax1.quiver(1, 0, -2, 1, 0, 0, length=1, color='black')  # dynamic obstacle velocity
ax1.set_title('(a) Point objects')
ax1.set_xlim(-4, 4); ax1.set_ylim(-4, 4); ax1.set_zlim(-4, 4)

### --- (b) Particles with velocities
ax2 = fig.add_subplot(142, projection='3d')
all_pts = np.vstack((static_pts, dynamic_pts))
velocities = generate_particles(all_pts, speed=0.5)
ax2.quiver(all_pts[:, 0], all_pts[:, 1], all_pts[:, 2],
           velocities[:, 0], velocities[:, 1], velocities[:, 2],
           length=0.5, normalize=True, color='orange')
ax2.scatter(*all_pts.T, facecolors='none', edgecolors='black', label='Particles')
ax2.text(2, 0, 4, 'Particles', backgroundcolor='lightgray')
ax2.set_title('(b) Particles in the local map')
ax2.set_xlim(-4, 4); ax2.set_ylim(-4, 4); ax2.set_zlim(-4, 4)

### --- (c) Voxel grid
ax3 = fig.add_subplot(143, projection='3d')
vox_origin = [-2, -2, -2]
vox_size = 1
for i in range(3):
    for j in range(3):
        for k in range(3):
            ax3.bar3d(vox_origin[0]+i, vox_origin[1]+j, vox_origin[2]+k,
                      vox_size, vox_size, vox_size, alpha=0.1, color='blue')
ax3.quiver(all_pts[:, 0], all_pts[:, 1], all_pts[:, 2],
           velocities[:, 0], velocities[:, 1], velocities[:, 2],
           length=0.5, normalize=True, color='orange')
ax3.set_title('(c) Voxel subspaces')
ax3.set_xlim(-4, 4); ax3.set_ylim(-4, 4); ax3.set_zlim(-4, 4)

### --- (d) Pyramid subspaces (Field of View)
ax4 = fig.add_subplot(144, projection='3d')
origin = np.array([0, 0, 0])
angles = np.linspace(-np.pi/6, np.pi/6, 6)
for theta in angles:
    for phi in angles:
        # Generate pyramid direction
        r = 4
        dx = r * np.cos(theta) * np.cos(phi)
        dy = r * np.cos(theta) * np.sin(phi)
        dz = r * np.sin(theta)
        ax4.plot([origin[0], dx], [origin[1], dy], [origin[2], dz], 'b', alpha=0.3)

# Plot one green FOV plane
ax4.plot_surface(np.array([[2, 2], [4, 4]]),
                 np.array([[0, 1], [0, 1]]),
                 np.array([[0, 0], [0, 0]]),
                 color='green', alpha=0.4)
ax4.text(3, 1, 0.5, 'Current FOV', backgroundcolor='lightgreen')
ax4.quiver(all_pts[:, 0], all_pts[:, 1], all_pts[:, 2],
           velocities[:, 0], velocities[:, 1], velocities[:, 2],
           length=0.5, normalize=True, color='orange')
ax4.set_title('(d) Pyramid subspaces')
ax4.set_xlim(-4, 4); ax4.set_ylim(-4, 4); ax4.set_zlim(-4, 4)

plt.tight_layout()
plt.show()
