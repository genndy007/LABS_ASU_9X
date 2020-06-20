def ParseFile(text): # File parsing
    arr = []
    for line in text:
        nums = line.split()
        arr.append([int(nums[0]), int(nums[1])])

    return arr

# finding degrees in graph
def CreateDictForDegree(graph):
    dct = {}      # Creating dictionary with start values
    for i in range(1, graph[0][0]+1): # of degrees
        dct[i] = 0
    return dct

def FindDegree(graph):
    degrees = CreateDictForDegree(graph)
    for i in range(1, len(graph)): # Through graph
        degrees[graph[i][0]] += 1  # incrementing vertex degree
        degrees[graph[i][1]] += 1  # if there is edge in it
    return degrees
#--------------------

def IntoPruferCode(graph):  ## Encoding tree into Prufer code
    num_vert = graph[0][0]     # Number of vertices
    possible = [num for num in range(1, num_vert+1)]  # Possible vertices
    code = ''     # Start value of Prufer code

    while len(graph) != 2:   # While there is not only one edge
        degrees = FindDegree(graph)   # Calculate degrees
        min_leaf = graph[0][0]   # Start value for minimal leaf
        for key in degrees:     # Looping through all vertices degrees 
            if degrees[key] == 1 and key in possible and key < min_leaf:
                min_leaf = key

        possible.remove(min_leaf)    # Remove minimal leaf from possible vertices

        for i in range(1, len(graph)): # Searching through graph
            if min_leaf in graph[i]:    # If found edge with minimal leaf
                if graph[i][0] == min_leaf:
                    code += str(graph[i][1])       # Adding other end of edge to code
                elif graph[i][1] == min_leaf:
                    code += str(graph[i][0])
                graph.pop(i)    # Delete edge from graph
                break

    return code


def DecodePrufer(code):
    codestring = ""
    for char in code:        # Delete everything that's not a number
        if char in '1234567890':
            codestring += char
    num_vert = len(codestring) + 2   # Prufer code has length (n-2)
    vertices = [num for num in range(1, num_vert+1)]  # All vertices list
    edges = []   # All edges

    for ind in range(len(codestring)):    # Going through every symbol in codestring
        v1 = int(codestring[ind])    # Every symbol is a vertex
        for v2 in vertices:  # Searching through all vertices
            if str(v2) not in codestring[ind:]:   # Finding what number not in further Prufer code
                edge = [v1, v2]    # Creating edge
                edges.append(edge)  # Adding it to all edges 
                vertices.remove(v2)  # Remove from vertices list
                break

    edges.append(vertices)    # Last edge in our tree comes from two vertices left in their list
                
    num_edges = len(edges)
    edges.insert(0, [num_vert, num_edges])   # Making list as we got it from file

    return edges

def CreateAdjacencyMatrix(source):   # Just creating adjacency matrix from received tree
    size = source[0][0]
    matrix = [[0 for i in range(size)] for j in range(size)]
    for k in range(1, len(source)):
        start = source[k][0]
        end = source[k][1]
        matrix[start - 1][end - 1] = 1
        matrix[end - 1][start - 1] = 1
    return matrix

def PrintMatrix(matrix):   # Printing by unpacking arrays
    for line in matrix:
        print(*line)

def OutMatrix(matr):   # Printing by hard work
    print('    ', end='')
    for i in range(len(matr)):
        print(f"v{i+1}  ", end='')
    print()
    for i in range(len(matr)):
        print(f"v{i+1}", end='')
        for j in range(len(matr[i])):
            print(f"   {matr[i][j]}", end='')
        print()

## Testing

while input("Type 'exit' to exit: ") != 'exit':
    what = input("Choose between 'Encode to Prufer'(e) and 'Decode to adjacency matrix'(d): ")
    while what != 'e' and what != 'd':
        what = input("Choose between 'Encode to Prufer'(e) and 'Decode to adjacency matrix'(d): ")
    
    raw = open('input.txt')
    graph = ParseFile(raw)
    
    if what == 'e':
        code = IntoPruferCode(graph)
        for char in code:
            print(f"{char} ", end='')
        print()
    if what == 'd':
        usercode = input('Type your code: ')
        tree = DecodePrufer(usercode)
        adjMatrix = CreateAdjacencyMatrix(tree)
        OutMatrix(adjMatrix) 
