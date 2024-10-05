import matplotlib.pyplot as plt
import numpy as np

# Example data (you can replace it with your data)
data = [0, 10, 10, 40, 48, 49, 50, 60, 60, 60, 60, 60, 80]
group2 = [8, 10, 11, 9, 12, 8, 10, 10, 8, 9, 11, 11, 9]

# Calculating quartiles and mean
Q1 = np.percentile(data, 25)
median = np.percentile(data, 50)
Q3 = np.percentile(data, 75)
mean = np.mean(data)

# Printing the values
print("Q1 (25th percentile):", Q1)
print("Median (50th percentile):", median)
print("Q3 (75th percentile):", Q3)
print("Mean:", mean)

data = [data, group2]
# Creating a box plot
plt.boxplot(data,labels=['Group 1', 'Group 2']) 

# Adding mean as a point on the graph
plt.scatter(1, mean, color='red', marker='_', label=f'Mean: {mean:.2f}')

# Adding a title, labels, and legend
plt.title('Box plot of your data with mean')
plt.ylabel('Values')
plt.legend()

# Display the plot
plt.show()
