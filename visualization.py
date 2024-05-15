import networkx as nx
import matplotlib.pyplot as plt
import ast

# Read data from a text file
output_data = []
with open("output_data.txt", "r") as file:
    for line in file:
        line = line.strip().split("\t")
        friend, user = line[0].split(",")
        common_friends = ast.literal_eval(line[1])
        output_data.append((friend.strip(), user.strip(), common_friends))

# Create a graph
G = nx.Graph()

# Add nodes and edges to the graph
for friend, user, common_friends in output_data:
    G.add_node(friend, label=friend, color="orange", size=3000)
    G.add_node(user, label=user, color="yellow", size=3000)
    if friend != user:  # Avoid adding self-loops
        G.add_edge(friend, user)
    for common_friend in common_friends:
        G.add_node(common_friend, label=common_friend, color="green", size=3000)
        if common_friend != friend and common_friend != user:  # Avoid adding self-loops
            G.add_edge(friend, common_friend)
            G.add_edge(user, common_friend)

# Visualize the graph with Kamada-Kawai layout
pos = nx.kamada_kawai_layout(G)
node_color = [G.nodes[n]["color"] for n in G.nodes()]
node_size = [G.nodes[n]["size"] for n in G.nodes()]

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_color=node_color, node_size=node_size)

# Draw edges
nx.draw_networkx_edges(G, pos)

# Draw labels
node_labels = nx.get_node_attributes(G, "label")
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=10, font_family="sans-serif", font_color="black")

# Legend for node colors
node_legend = {
    "Friend": "orange",
    "User": "yellow",
    "Common Friend": "green"
}
plt.legend(handles=[plt.Line2D([0], [0], marker="o", color=color, label=label, markersize=8, linestyle="None") 
                    for label, color in node_legend.items()], loc="upper left")

plt.title("Twitter User - Mutual Friends Analysis")
plt.axis("off")  # Hide axis
plt.show()
