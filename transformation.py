import numpy as np

def transform_points(points, R, t):
    """
    Transform multiple points from one frame to another.

    Args:
    - points: Nx3 numpy array of points [x, y, z]
    - R: 3x3 rotation matrix
    - t: 1x3 translation vector

    Returns:
    - transformed_points: Nx3 numpy array of transformed points [x', y', z']
    """
    # Ensure points is a numpy array
    points = np.array(points)
    print(points.T)

    # Apply the transformation
    transformed_points = np.dot(R, points.T).T + t

    return transformed_points

# Example usage:
if __name__ == "__main__":
    # Example transformation parameters
    R = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])  # Identity rotation (no rotation)
    t = np.array([1, 0, 0])  # Translation vector

    # Example points to transform
    points = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    # Transform points
    transformed_points = transform_points(points, R, t)

    #print("Original Points:\n", points)
    #print("Transformed Points:\n", transformed_points)
