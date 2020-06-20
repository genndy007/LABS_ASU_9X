def ParseFile(filename):
    file = open(filename)       # Parse file, as usual
    graph = []
    for line in file:
        words = line.split()
        for i in range(len(words)):
            words[i] = int(words[i])
        graph.append(words)
    return graph

def FindDegrees(graph):
    degrees = {i:[0,0] for i in range(1, graph[0][0] + 1)}
    first = True
    for edge in graph:            # Discovering degrees in and out
        if first:
            first = False
            continue
        v1, v2, w = edge
        degrees[v1][1] += 1
        degrees[v2][0] += 1
    return degrees

def FindSourceAndSink(graph):
    degrees = FindDegrees(graph)
    source = None       
    sink = None
    for key in degrees:
        if degrees[key][0] == 0:    # it is source if in-degree is 0
            source = key
        if degrees[key][1] == 0:    # it is sink if out-degree is 0
            sink = key
    return source, sink


def StartCapacity(graph):
    capacity = [[0 for i in range(graph[0][0])] for i in range(graph[0][0])]
    for edge in graph:
        if len(edge) == 2:        # Calculating start capacity for graph
            continue              # Capacity is in form of matrix
        v1, v2, w = edge          # c[i][j] is capacity for edge [i, j]
        capacity[v1 - 1][v2 - 1] = w
    return capacity

def StartMarks(source, numVert):
    marks = {source:[float('inf'), -1]}
    for i in range(1, numVert + 1):
        if i == source:        # Creating default marks for our vertices
            continue
        marks[i] = None
    return marks

def FindNeighbors(graph):
    neighbors = {i:[] for i in range(1, graph[0][0] + 1)}
    for edge in graph:
        if len(edge) == 2:       # Finding neighbors for all vertices
            continue             # so we know where we can move to
        v1 = edge[0]
        v2 = edge[1]
        neighbors[v1].append(v2)
        neighbors[v2].append(v1)
    return neighbors


def FordFulkerson(graph):    # That nightmare
    # Initialization
    source, sink = FindSourceAndSink(graph)   # declaring source and sink
    neighbors = FindNeighbors(graph)         # declaring neighbors
    print("Paths that taken part in maximal flow:")
    start = StartCapacity(graph)        # Creating start capacity and capacity to work on 
    capacity = StartCapacity(graph)     # so we calculate the flow for every edge
    numVert = graph[0][0]
    graph.pop(0)
    summaryFlow = 0
    noAugmentingPaths = False
    
    # Main loop
    while not noAugmentingPaths:    # while there are possible paths that we haven't passed through yet
        # Step 1
        i = source    
        marks = StartMarks(source, numVert)   # Declaring start marks and start container of path
        verticesInPath = [source]             # Marks are of two elements: free capacity and a parent
        # Step 2
        while True:     
            whereCanGo = []
            
            for neighbor in neighbors[i]:         # Checking for vertices we can go to
                if capacity[i - 1][neighbor - 1] > 0 and marks[neighbor] is None: 
                    whereCanGo.append(neighbor)   # Vertex should have positive not used capacity and 
                                                  # should have no mark

            if len(whereCanGo) != 0:
                # Step 3
                k = whereCanGo[0]
                maxValue = capacity[i - 1][k - 1] 
                for j in range(len(whereCanGo)):   # Here we find maximum capacity vertex that we able 
                    if capacity[i - 1][whereCanGo[j] - 1] > maxValue:  # to go into
                        k = whereCanGo[j]
                        maxValue = capacity[i - 1][k - 1]

                marks[k] = [maxValue, i]       # Set a mark for vertex we chose


                if k == sink:   # If we reached our sink - stop going deeper
                    verticesInPath.append(k)
                    # Go to step 5
                    break
                else:
                    i = k     # If not, continue our odyssey to the sink
                    verticesInPath.append(k)

            else:
                # Step 4
                if i == source:  # If we are at source and there is no more possible paths,
                    noAugmentingPaths = True   # we stop our paths search
                    # Go to step 6
                    break
                else:
                    r = marks[i][1]    # Or if we can't go anywhere from a vertex,
                    neighbors[r].remove(i)   # we go back and delete it from our neighbors
                    i = r
        
        # Step 5
        flow = marks[source][0]
        if len(verticesInPath) == 1:
            break
        

        for vertex in verticesInPath:   # Here we calculate flow through the path we found
            if marks[vertex][0] < flow:  # Flow is equal ro minimal free capacity in path
                flow = marks[vertex][0]

        print(f"Path: {verticesInPath} with flow of {flow}")
        summaryFlow += flow

        for e in range(len(verticesInPath) - 1):   # Changing capacity matrix by the flow size (edge is [i, j])
            capacity[verticesInPath[e] - 1][verticesInPath[e + 1] - 1] -= flow   # c[i][j] -= flow
            capacity[verticesInPath[e + 1] - 1][verticesInPath[e] - 1] += flow   # c[j][i] += flow  

    ### Now print flow through every vertex
    flow = CalculateFlow(start, capacity, graph)
    FlowPrinter(flow, graph)

    return summaryFlow
    


def CalculateFlow(start, capacity, graph):
    flow = []
    for edge in graph:         # Calculate the flow for every edge in way:
        v1, v2, w = edge       # Let C[] is start capacity and c[] is capacity at the end
        a = start[v1 - 1][v2 - 1] - capacity[v1 - 1][v2 - 1]  # So a = C[i][j] - c[i][j]
        b = start[v2 - 1][v1 - 1] - capacity[v2 - 1][v1 - 1]  # And b = C[j][i] - c[j][i]
        if a > 0:
            flow.append(a)
        else:
            flow.append(b)

    return flow


def FlowPrinter(flow, graph):
    print("Flows through graph vertices:")    # Here I make output to the terminal 
    print("Edge     Flow")                    # for user to observe it in comfortable way
    for i in range(len(graph)):
        print(f"{graph[i][0]} - {graph[i][1]}    {flow[i]} of {graph[i][2]}")


                
    
    

#### TESTING
filename = 'input.txt'
graph = ParseFile(filename)
source, sink = FindSourceAndSink(graph)
print("Source vertex:", source)
print("Sink vertex:", sink)
succ = FordFulkerson(graph)
print(f"Maximal flow: {succ}")
 