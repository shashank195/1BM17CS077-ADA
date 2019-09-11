from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdgeToVertex(self, vertex, edge):
        self.graph[vertex].append(edge)
    
    def BFS(self, s):
        visited = [0] * len(self.graph)
        queue = []

        queue.append(s)
        visited[s] = 1

        while queue:
            item = queue.pop(0)
            print(item, end=" ")

            for i in self.graph[item]:
                if visited[i] == 0:
                    queue.append(i)
                    visited[i] = 1

g = Graph()
g.addEdgeToVertex(0, 1) 
g.addEdgeToVertex(0, 2) 
g.addEdgeToVertex(1, 2) 
g.addEdgeToVertex(2, 0) 
g.addEdgeToVertex(2, 3) 
g.addEdgeToVertex(3, 3) 

print(g.graph)
g.BFS(2)

# make a dict out of an adjacency matrix