# 1. Adjacency Matrix Implementation:
# Create a Python class that initializes an n ×n matrix with 0s.
# Add a method add edge(u,v) that sets matrix[u][v] (and matrix[v][u] for undirected).
# Print the matrix in a clear format.

class Adj_Matrix:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        # For undirected graph
        self.adj_matrix[v][u] = 1 

    def display(self):
        for row in self.adj_matrix:
            print(row)

if __name__ == "__main__":
    graph = Adj_Matrix(5)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(3, 1)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(3, 0)
    graph.add_edge(3, 0)

    print("Adjacency Matrix:")
    graph.display()