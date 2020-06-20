class Graph:
    def __init__(self, v, adj):
        self.v = v
        self.adj = adj

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def greedyColoring(self):
        result = [0]

        for u in range(1, self.v):
            result[u] = -1
        
        available = []
        for cr in range(self.v):
            available[cr] = False

        for u in range(1, self.v):
            i = []
            for 

