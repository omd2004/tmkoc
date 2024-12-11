import heapq


def network_delay_time(n, edges, k):
    # Create a graph as an adjacency list
    graph = {i: [] for i in range(1, n + 1)}
    for u, v, w in edges:
        graph[u].append((v, w))

    # Min-heap to keep track of the shortest distance to each node
    heap = [(0, k)]  # (time, node)
    shortest_time = {i: float('inf') for i in range(1, n + 1)}
    shortest_time[k] = 0

    # Perform Dijkstra's algorithm
    while heap:
        current_time, node = heapq.heappop(heap)

        # Skip processing if we've already found a shorter path
        if current_time > shortest_time[node]:
            continue

        # Update neighboring nodes
        for neighbor, time in graph[node]:
            new_time = current_time + time
            if new_time < shortest_time[neighbor]:
                shortest_time[neighbor] = new_time
                heapq.heappush(heap, (new_time, neighbor))

    # Find the maximum time to reach any node
    max_time = max(shortest_time.values())
    return max_time if max_time != float('inf') else -1


# Example usage
n = 4
edges = [
    (2, 1, 1),  # Edge from node 2 to node 1 with weight 1
    (2, 3, 1),  # Edge from node 2 to node 3 with weight 1
    (3, 4, 1)  # Edge from node 3 to node 4 with weight 1
]
k = 2  # Start node

result = network_delay_time(n, edges, k)
print("Time for all nodes to receive the signal:", result)
