# Define the points
points = [(0, 4), (2, 2), (4, 6), (5, 3), (7, 5)]

# Implement a basic sorting algorithm (bubble sort) based on y-values
n = len(points)
for i in range(n - 1):
    for j in range(0, n - i - 1):
        if points[j][1] > points[j + 1][1]:
            # Swap the points
            points[j], points[j + 1] = points[j + 1], points[j]

# Print the sorted points
print("Sorted points based on y-values:")
for point in points:
    print(point)
