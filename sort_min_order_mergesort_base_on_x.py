def merge_sort(points):
    if len(points) <= 1:
        return points
    
    # Divide the list into two halves
    mid = len(points) // 2
    left_half = points[:mid]
    right_half = points[mid:]
    
    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the sorted halves
    sorted_points = []
    left_index = right_index = 0
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index][0] < right_half[right_index][0]:
            sorted_points.append(left_half[left_index])
            left_index += 1
        else:
            sorted_points.append(right_half[right_index])
            right_index += 1
    
    sorted_points.extend(left_half[left_index:])
    sorted_points.extend(right_half[right_index:])
    
    return sorted_points

# Example usage:
points = [(0, 4), (2, 2), (4, 6), (5, 3), (7, 5),(-3,0)]
sorted_points = merge_sort(points)
print("Sorted points based on x-values:")
for point in sorted_points:
    print(point)
