# 6. Complexity Comparison:
# Compare adding edges in adjacency matrices vs. adjacency lists in terms of time complexity.

import time
import random
import matplotlib.pyplot as plt

def time_adjacency_matrix_add(n, num_edges):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    start_time = time.time()
    for _ in range(num_edges):
        u = random.randint(0, n-1)
        v = random.randint(0, n-1)
        matrix[u][v] = 1
    end_time = time.time()
    
    return end_time - start_time

def time_adjacency_list_add(n, num_edges):
    adj_list = [[] for _ in range(n)]
    
    start_time = time.time()
    for _ in range(num_edges):
        u = random.randint(0, n-1)
        v = random.randint(0, n-1)
        adj_list[u].append(v)
    end_time = time.time()
    
    return end_time - start_time

sizes = [100, 500, 1000, 2000, 3000, 5000, 10000]
matrix_times = []
list_times = []

for n in sizes:
    edges_to_add = int(n * 10)
    
    matrix_time = time_adjacency_matrix_add(n, edges_to_add)
    list_time = time_adjacency_list_add(n, edges_to_add)
    
    matrix_times.append(matrix_time)
    list_times.append(list_time)
    
    print(f"Size {n}: Matrix: {matrix_time:.6f}s, List: {list_time:.6f}s")

plt.figure(figsize=(10, 6))
plt.plot(sizes, matrix_times, 'o-', label='Adjacency Matrix')
plt.plot(sizes, list_times, 'o-', label='Adjacency List')
plt.xlabel('Number of Vertices (n)')
plt.ylabel('Time (seconds)')
plt.title('Time Complexity: Adding Edges')
plt.legend()
plt.grid(True)
plt.show()

# In terms of time complexity, the adjacency list is generally faster for adding edges
# in sparse graphs, while the adjacency matrix is faster for dense graphs.