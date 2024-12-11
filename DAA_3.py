def floyd_warshall(graph):
    # Number of vertices
    n = len(graph)

    # Initialize distance matrix with the input graph
    dist = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0  # Distance to itself is zero
            elif graph[i][j] != 0:
                dist[i][j] = graph[i][j]  # Distance is the edge weight

    # Floyd-Warshall algorithm
    for k in range(n):  # Intermediate nodes
        for i in range(n):  # Source node
            for j in range(n):  # Destination node
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


# Example input graph: Adjacency matrix representation
# 0 means no direct connection between the cities
graph = [
    [0, 4, 0, 0, 0, 0],
    [4, 0, 8, 0, 0, 0],
    [0, 8, 0, 7, 0, 4],
    [0, 0, 7, 0, 9, 14],
    [0, 0, 0, 9, 0, 10],
    [0, 0, 4, 14, 10, 0]
]

# Compute shortest paths
shortest_paths = floyd_warshall(graph)

# Display the shortest path matrix
print("Shortest paths between all pairs of cities:")
for row in shortest_paths:
    print(row)
