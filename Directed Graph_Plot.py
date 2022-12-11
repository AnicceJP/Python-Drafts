import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edges_from([('a', 'b'), ('a','d'), ('a', 'c'), ('a', 'e'), ('b', 'd'), ('c','d'), ('c','e'), ('d', 'e')])

pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, node_size=500)
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black')
nx.draw_networkx_labels(G, pos)

plt.show()
