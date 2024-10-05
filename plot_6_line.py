import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add nodes
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
G.add_nodes_from(nodes)

# Add edges based on the lines
edges = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F'), ('F', 'G'), ('G', 'H'), ('H', 'I'), ('I', 'J'), ('J', 'A'), ('A', 'E'), ('C', 'H'), ('B', 'G')]
G.add_edges_from(edges)

# Draw the graph
nx.draw(G, with_labels=True, node_color='lightblue', node_size=500, font_size=10)

# Show the plot
plt.show()