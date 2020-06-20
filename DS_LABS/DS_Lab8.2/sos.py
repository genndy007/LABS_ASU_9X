def ParseFile(filename):
    arr = []
    file = open(filename)
    first = True
    for line in file:
        if first:
            first = False
            n, m = line.split()
            arr.append([int(n), int(m)])
            continue
        v, u, w = line.split()
        arr.append([int(v), int(u), int(w)])
    return arr


def PrimAlgorithm(graph):
    spanSize = graph[0][0] - 1  # Spanning tree has size of (n-1) edges
    graph.pop(0)
    
    firstEdge = graph[0]   
    for edge in graph:                   # Selecting minimal weight edge
        if edge[2] < firstEdge[2]:
            firstEdge = edge
    spanningTree = [firstEdge]
    connectedVertices = [firstEdge[0], firstEdge[1]]

    while len(spanningTree) < spanSize:
        edgeToAdd = None
        for edge in graph:
            if edgeToAdd is None:
                if (edge[0] in connectedVertices or edge[1] in connectedVertices) and edge not in spanningTree:
                    edgeToAdd = edge
                continue

            if (edge[0] in connectedVertices or edge[1] in connectedVertices) and edge[2] < edgeToAdd[2] and edge not in spanningTree:
                edgeToAdd = edge
        connectedVertices.append(edgeToAdd[0])
        connectedVertices.append(edgeToAdd[1])
        spanningTree.append(edgeToAdd)
    
    return spanningTree

##### TESTING
filename = 'input.txt'
graph = ParseFile(filename)
spanningTree = PrimAlgorithm(graph)

print("Edge    Weight")
for edge in spanningTree:
    print(f"{edge[0]} - {edge[1]}    {edge[2]}") 