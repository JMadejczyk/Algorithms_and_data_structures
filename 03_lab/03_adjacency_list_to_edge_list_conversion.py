# 3. Adjacency List to Edge List Conversion:
# Write a function that takes an adjacency list and returns a list of edges. For an undirected
# graph, ensure you don’t duplicate edges.

def adjacency_list_to_edge_list(adj_list):    
    edge_list = []
    processed_edges = set()
    
    for vertex, neighbors in adj_list.items():
        for neighbor in neighbors:
            edge = tuple(sorted([vertex, neighbor]))
            
            if edge not in processed_edges:
                edge_list.append(edge)
                processed_edges.add(edge)
                
    return edge_list

if __name__ == "__main__":
    adjacency_list = {
        0: [1, 2, 4],
        1: [0, 2],
        2: [0],
        3: [1, 2, 3, 4],
        4: [4]
    }
    
    edge_list = adjacency_list_to_edge_list(adjacency_list)
    print("Edge List:", edge_list)