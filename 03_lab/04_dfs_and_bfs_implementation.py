# 4. DFS and BFS Implementation:
# Implement both in a Python class with adjacency lists. Demonstrate how they visit
# vertices in different orders.

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
    
    def bfs(self, start_vertex):
        visited = set()
        queue = [start_vertex]
        visited.add(start_vertex)
        result = []
        
        while queue:
            vertex = queue.pop(0)
            result.append(vertex)
            
            if vertex in self.graph:
                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
        
        return result

if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)
    
    print("DFS starting from vertex 2:", graph.dfs(2))
    print("BFS starting from vertex 2:", graph.bfs(2))