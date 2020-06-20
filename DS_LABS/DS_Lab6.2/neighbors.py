def ParseFile(text): # File parsing
    arr = []
    for line in text:
        nums = line.split()
        arr.append([int(nums[0]), int(nums[1])])

    return arr

def CreateDictOfNeighbors(graph):   # Creating dictionary of neighbors for knowing which colour possible or not
    num_vert = graph[0][0]
    di = {k: [] for k in range(1, num_vert+1)}
    first_line = True
    for edge in graph:
        if first_line:
            first_line = False
            continue
        v1 = edge[0]
        v2 = edge[1]
        di[v1].append(v2)
        di[v2].append(v1)
    return di

def NeighborColouring(di):   # Colouring itself
    colours = {k: -1 for k in range(1, len(di) + 1)}   # First state of colours for every vertex - unknown (-1) 

    for vertex in colours:     # Finding appropriate colour for every vertex
        for i in range(len(di)):  # Checking every possible colour
            notThis = False
            for neigh in di[vertex]:   # Checking every neighbor vertex for current
                if colours[neigh] == i:  # If neighbor with some color already present, then it's not our choice
                    notThis = True
            if notThis:     # Not our choice, skip this colour
                continue
            colours[vertex] = i   # Setting colour
            break
    return colours

def printer(colours):
    for vert in colours:
        print(f'Vertex {vert}: Colour {colours[vert] + 1}')

### TESTING

raw = open('input.txt')
graph = ParseFile(raw)
di = CreateDictOfNeighbors(graph)

colours = NeighborColouring(di)

printer(colours)
