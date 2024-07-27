import heapq
import networkx as nx
import matplotlib.pyplot as plt

# Create graph
G = nx.Graph()
stations = ["Головний вокзал", "Площа Ринок", "Опера", "Високий замок", "Політехніка", "Медичний університет"]
G.add_nodes_from(stations)

edges = [
    ("Головний вокзал", "Площа Ринок", 2),
    ("Площа Ринок", "Опера", 3),
    ("Опера", "Високий замок", 4),
    ("Високий замок", "Політехніка", 5),
    ("Політехніка", "Медичний університет", 6),
    ("Медичний університет", "Головний вокзал", 7),
    ("Головний вокзал", "Опера", 8),
    ("Площа Ринок", "Високий замок", 9),
]
G.add_weighted_edges_from(edges)

def dijkstra(graph, start):
    distances = {node: float("infinity") for node in graph.nodes}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, attributes in graph[current_node].items():
            weight = attributes["weight"]
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

all_distances = {node: dijkstra(G, node) for node in G.nodes}

print("Найкоротші відстані між усіма парами вершин:")
for source in all_distances:
    for target in all_distances[source]:
        print(f"Від {source} до {target}: відстань {all_distances[source][target]}")

pos = nx.spring_layout(G)
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

edge_labels = {(u, v): f'{d["weight"]}' for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Схема руху громадського транспорту Львова з нумерацією ребер")
plt.show()