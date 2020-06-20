def ParseFile(text):
    arr = []
    for line in text:
        nums = line.split()
        arr.append([int(nums[0]), int(nums[1])])

    return arr

def CreateAdjacencyMatrix(graph):
    num_vert = graph[0][0]
    matrix = [[0 for i in range(num_vert)] for i in range(num_vert)]
    for i in range(num_vert):
        matrix[i][i] = 1

    first_line = True
    for edge in graph:
        if first_line:
            first_line = False
            continue
        v1 = edge[0] - 1
        v2 = edge[1] - 1
        matrix[v1][v2] = 1
        matrix[v2][v1] = 1

    return matrix

def GraphColoringWithMatrix(adjMatrix):
    k = 1
    num_vert = len(adjMatrix)
    coloured = []
    colours = {}
    for i in range(num_vert):
        colours[k] = []
        if i in coloured:
            continue
        colours[k].append(i)
        coloured.append(i)
        while (0 in adjMatrix[i]):
            for j in range(i+1, num_vert-1):
                if adjMatrix[i][j] == 0 and j not in coloured:
                    break
            if j == num_vert:
                break
            colours[k].append(j)
            coloured.append(j)
            # disjunction
            for v in range(num_vert):
                adjMatrix[i][v] |= adjMatrix[j][v]
        k += 1
    return colours


def ColoringDeleting(graph):
    num_vert = graph[0][0]
    uncoloured = list(range(1, num_vert+1))
    graph.pop(0)
    while len(graph) != 0:
        for i in range(1, num_vert+1):
            if i not in uncoloured:
                continue
            oneColour = [i]
            uncoloured.remove(i)
            possibleChoose = list(range(1, num_vert+1))
            while len(possibleChoose) != 0:
                for edge in graph:
                    if edge[0] in possibleChoose and edge[1] in oneColour:
                        possibleChoose.remove(edge[0])
                    if edge[1] in possibleChoose and edge[0] in oneColour:
                        possibleChoose.remove(edge[1])
                
                oneColour.append(possibleChoose[0])
                uncoloured.remove(possibleChoose[0])
            for edge in graph:
                for vert in oneColour:
                    if vert in edge:
                        graph.remove(edge)
                        break
            print(oneColour)
            


## TESTING
raw = open('input.txt')
graph = ParseFile(raw)
adjMatrix = CreateAdjacencyMatrix(graph)
ColoringDeleting(graph)