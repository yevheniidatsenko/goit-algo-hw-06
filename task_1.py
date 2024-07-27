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

# Аналіз графа
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_centrality = nx.degree_centrality(G)

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступінь вершин:")
for node, degree in degree_centrality.items():
    print(f"{node}: {degree:.2f}")