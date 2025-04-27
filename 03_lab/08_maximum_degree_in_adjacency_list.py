# 8. Maximum Degree in Adjacency List:
# Write a function to find the maximum degree among all vertices in an adjacency list.

def maximum_degree(adj_list):
    max_degree = 0
    max_vertex = -1

    for vertex, neighbors in adj_list.items():
        degree = len(neighbors)
        if degree > max_degree:
            max_degree = degree
            max_vertex = vertex

    return max_vertex, max_degree

if __name__ == "__main__":
    adjacency_list = {
        0: [1, 2, 4],
        1: [0, 2],
        2: [0],
        3: [1, 2, 3, 4],
        4: [4]
    }

    vertex, degree = maximum_degree(adjacency_list)
    print(f"Vertex with maximum degree: {vertex}; Degree is: {degree}")