# 5. Path Existence:
# Write a function that uses DFS to determine if there is a path between two vertices.

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
    
    def dfs(self, start_vertex):
        visited = set()
        result = []
        
        def dfs_recursive(vertex):
            visited.add(vertex)
            result.append(vertex)
            
            if vertex in self.graph:
                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        dfs_recursive(neighbor)
        
        dfs_recursive(start_vertex)
        return result
    
    def path_exists(self, start_vertex, end_vertex):
        if start_vertex == end_vertex:
            return True
            
        visited = set()
        
        def dfs_recursive(vertex):
            visited.add(vertex)
            
            if vertex in self.graph:
                for neighbor in self.graph[vertex]:
                    if neighbor == end_vertex:
                        return True
                    if neighbor not in visited:
                        if dfs_recursive(neighbor):
                            return True
            return False
        
        return dfs_recursive(start_vertex)

if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)
    
    start_vertex = 0
    end_vertex = 3
    if graph.path_exists(start_vertex, end_vertex):
        print(f"A path exists between {start_vertex} and {end_vertex}.")
    else:
        print(f"No path exists between {start_vertex} and {end_vertex}.")
        
    start_vertex = 1
    end_vertex = 4
    if graph.path_exists(start_vertex, end_vertex):
        print(f"A path exists between {start_vertex} and {end_vertex}.")
    else:
        print(f"No path exists between {start_vertex} and {end_vertex}.")