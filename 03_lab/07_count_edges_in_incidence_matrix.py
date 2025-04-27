# 7. Count Edges in Incidence Matrix:
# Given an incidence matrix, determine how many edges the graph has. (Check how many columns are used.)

def count_edges(incidence_matrix):
    if len(incidence_matrix) == 0 or not incidence_matrix:
        return 0    
    return len(incidence_matrix[0])

if __name__ == "__main__":
    example_matrix = [
        [1, 1, 0, 0], 
        [1, 1, 1, 1],
        [0, 1, 0, 0]
    ]
    
    print(f"Number of edges in the graph: {count_edges(example_matrix)}")