import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вершин (станцій)
stations = ["Головний вокзал", "Площа Ринок", "Опера", "Високий замок", "Політехніка", "Медичний університет"]
G.add_nodes_from(stations)

# Додавання ребер (маршрутів)
edges = [
    ("Головний вокзал", "Площа Ринок"),
    ("Площа Ринок", "Опера"),
    ("Опера", "Високий замок"),
    ("Високий замок", "Політехніка"),
    ("Політехніка", "Медичний університет"),
    ("Медичний університет", "Головний вокзал"),
    ("Головний вокзал", "Опера"),
    ("Площа Ринок", "Високий замок"),
]

G.add_edges_from(edges)

# Розміщення вершин на графі
pos = nx.spring_layout(G)

# Нумерація ребер
edge_labels = {
    ("Головний вокзал", "Площа Ринок"): "1",
    ("Площа Ринок", "Опера"): "2",
    ("Опера", "Високий замок"): "3",
    ("Високий замок", "Політехніка"): "4",
    ("Політехніка", "Медичний університет"): "5",
    ("Медичний університет", "Головний вокзал"): "6",
    ("Головний вокзал", "Опера"): "7",
    ("Площа Ринок", "Високий замок"): "8",
}

# Малювання графа
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="lightblue",
    node_size=2000,
    edge_color="gray",
    font_size=15,
    font_color="darkgreen",
)

# Додавання нумерації ребер
nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=edge_labels,
    font_color="red",
    font_size=12,
)

plt.title("Схема руху громадського транспорту Львова з нумерацією ребер")
plt.show()

def dfs(graph, start):
    visited = set()
    stack = [start]
    path = []
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            path.append(node)
            for neighbor in graph.neighbors(node):
                if neighbor not in visited:
                    stack.append(neighbor)
                    
    return path

def bfs(graph, start):
    visited = set()
    queue = [start]
    path = []
    
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            path.append(node)
            for neighbor in graph.neighbors(node):
                if neighbor not in visited:
                    queue.append(neighbor)
                    
    return path

start_node = "Головний вокзал"

dfs_path = dfs(G, start_node)
bfs_path = bfs(G, start_node)

print("DFS шлях:", dfs_path)
print("BFS шлях:", bfs_path)