# Implement Dijkstra's algorithm and test it on the example graph provided.
# Verify the shortest path distances from node A.

# Graph Edges and Weights
# Edge Weight
# A → B 4
# A → C 2
# B → C 1
# B → D 5
# C → D 8

import heapq

def dijkstra(graph, start):

    # Initialize distances and priority queue
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]  # (distance, node)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Nodes can only be added once to the priority queue
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

result = dijkstra({
    'A': {'B': 4, 'C': 2},
    'B': {'C': 1, 'D': 5},
    'C': {'D': 8},
    'D': {}
}, 'A')

print("Shortest path distances from node A:", result)