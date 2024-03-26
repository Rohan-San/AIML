import networkx as nx
import matplotlib as plt
from collections import deque

def bfs(graph,start):
    visited = set()
    queue = deque([start])
    while queue:
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)
            queue.extend(graph[vertex] - visited)

graph = {
    'A': set(['B','C']),
    'B': set(['A','D','E']),
    'C': set(['A','F']),
    'D': set(['B']),
    'E': set(['B','F']),
    'F': set(['C','E']),
    'G': set(['A','C']),
}

graph['C'].add('G')

G = nx.Graph(graph)
plt.figure(figsize = (8,6))
pos = nx.spring_layout(G)
nx.draw(G,pos,with_labels=True,node_color='skyblue',node_size=1000,font_size=12,font_weight='bold',edge_color='gray')
plt.title('Initial Network Diagram')
plt.show()

print("BFS Traversal")
bfs(graph,'A')
