import os
import matplotlib
matplotlib.use('Agg')  # server-only mode, no GUI
import matplotlib.pyplot as plt
import networkx as nx

############################################################
# Loading edges of the Graph from a file: edges.txt
curr_dir = os.path.dirname(__file__)  # get the current directory of this file

edges_fil = os.path.join(curr_dir, "edges.txt")  # path to edges.txt
graph_visual_fil = os.path.join(curr_dir, "graph_visual.png")  # path to save graph visualization

# Initialize directed graph
g = nx.DiGraph()

############################################################
# STEP 1 - Create Graph
# Read edges from the txt file
edges = []

with open(edges_fil, 'r') as file:
    for line in file.readlines():
        node1, node2, weight = line.strip().split(",")
        weight = int(weight)
        edges.append((node1.strip(), node2.strip(), weight))

print("Edges:", edges)
g.add_weighted_edges_from(edges)

# Print all nodes
print("Nodes:", list(g.nodes))

# Saving graph as an image, for review
pos = nx.circular_layout(g)  # layout for visualization
nx.draw_networkx(g, pos)
labels = nx.get_edge_attributes(g, 'weight')
nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

plt.savefig(graph_visual_fil)
print(f"Graph visualization saved as {graph_visual_fil}")

############################################################
# STEP 2 - Find and Display Shortest Paths
print("\nShortest paths between all node pairs:")

for n1 in g.nodes:
    for n2 in g.nodes:
        if n1 != n2:
            try:
                shortest_path = nx.shortest_path(g, source=n1, target=n2, weight='weight')
                shortest_path_weight = nx.shortest_path_length(g, source=n1, target=n2, weight='weight')
                print(f"Shortest path from {n1} to {n2}: {' -> '.join(shortest_path)} (Weight: {shortest_path_weight})")
            except nx.NetworkXNoPath:
                print(f"No path from {n1} to {n2}")

