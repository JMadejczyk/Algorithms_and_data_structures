# 2. Incidence Matrix from Edge List:
# Given a list of edges, build an incidence matrix. Print out the matrix and explain how
# each column corresponds to an edge.

class Incidence_Matrix:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = len(edges)
        self.inc_matrix = [[0 for _ in range(self.edges)] for _ in range(self.vertices)]

    def add_edge(self, edge, index):
        u, v = edge
        self.inc_matrix[u][index] = 1
        self.inc_matrix[v][index] = 1

    def display(self):
        for row in self.inc_matrix:
            print(row)
        print("\nEach column corresponds to an edge in the graph.")
        print("\nIncidence Matrix:")
        for i in range(self.edges):
            edge_str = f"Edge #{i}: "
            for j in range(self.vertices):
                edge_str += f"{self.inc_matrix[j][i]} "
            print(edge_str.strip())
        
if __name__ == "__main__":
    vertices = 5
    edges_list = [
    (0, 1),
    (0, 2),
    (1, 3),
    (1, 4),
    (2, 3),
    (3, 4),
    (4, 0),
    (4, 1),
    (4, 2),
    (4, 3)
    ]
    graph = Incidence_Matrix(vertices, edges_list)
    for index, edge in enumerate(edges_list):
        graph.add_edge(edge, index)

    graph.display()