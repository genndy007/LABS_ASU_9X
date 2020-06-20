from collections import defaultdict
from itertools import permutations
import sys

def Invertor(color):
    return 2 if color == 1 else 1

class Graph:
    def __init__(self, numVert, numEdges):
        self.numVert = numVert  # Vertices
        self.numEdges = numEdges  # Edges
        self.graph = defaultdict(list) # Default dictionary never raises a KeyError, instead it returns a list 
        self.colors = [0 for k in range(self.numVert)]  # Setting start colors

    # Creating an adjacency matrix
    def CreateAdjMatrix(self):
        matrix = [[0 for k in range(self.numVert)] for k in range(self.numVert)]
        for v in range(self.numVert):  # Checking every vertex
            for u in self.graph[v]:    # Checking neighbors
                matrix[u][v] = 1
                matrix[v][u] = 1
        return matrix

    # Adding an edge
    def AddEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    
    # Search through the graph and setting colors for vertices
    def DepthFirstSearch(self, v, color):
        self.colors[v] = color   # Set a color to a vertex

        for i in self.graph[v]:  # Checking neighbors of vertex 
            if not self.colors[i]:  # If neighbor is not coloured
                self.DepthFirstSearch(i, Invertor(color))  # We go DFS in it
            elif self.colors[i] == color:  # If colors are equal then we have not a bipartite graph
                print("Graph in file is not bipartite\nTerminating...")
                sys.exit()

    def SetColors(self):  # Setting colors with DFS
        for i in range(self.numVert):   # Checking every vertex
            if not self.colors[i]:      # If vertex is not coloured  
                self.DepthFirstSearch(i, 1)   # Go DFS into it

    def FindPerfectMatching(self):
        colordictionary = {1: [], 2: []}   # Create dictionary with colors
        for num, color in enumerate(self.colors):   # Putting vertices into it 
            colordictionary[color].append(num)
        counter = len(colordictionary[1])
        not_balanced = False
        if counter != len(colordictionary[2]):   # If there are not equal dictionaries
            colordictionary[1], colordictionary[2] = colordictionary[2], colordictionary[1]
            not_balanced = True

        successful = []  # Successful matchings
        for perm in permutations(range(counter)):  # Checking every permutation
            matches = True  # Suppose all matchings are matching each other 
            if not_balanced:  # If graph is not balanced, we check through every matching
                index = -1
            else: # If it's balanced, everything's ok and it's easy to find matchings
                index = 0
            for v1, v2 in enumerate(perm[:index]):  # Checking matchings
                if colordictionary[2][v2] not in self.graph[colordictionary[1][v1]]:
                    matches = False
                    break  # If there is no matching we deny this permutation 
            if matches:   # if matching is good we combine it's parts
                firstPart, secondPart = map(lambda x: colordictionary[1][x], range(counter)), map(lambda x: colordictionary[2][x], perm)
                bipartiteMatching = tuple(zip(firstPart, secondPart))  # Assigning those parts to a matching
                successful.append(bipartiteMatching)
        return successful

def MatrixPrinter(matrix):
    numVert = len(matrix)
    print("   ", end='')
    for i in range(numVert):
        print(f"{i+1} ", end='')
    print()
    for i in range(numVert):
        print(f'{i+1} ', *matrix[i])

inputFile = open('input.txt')

firstLine = inputFile.readline() 
firstArr = firstLine.split()   # Finding numbers of vertices
numVert = int(firstArr[0])     # and edges
numEdges = int(firstArr[1])

graph = Graph(numVert, numEdges)

for line in inputFile:   # Adding edges
    v1, v2 = line.split()
    v1 = int(v1) - 1
    v2 = int(v2) - 1
    graph.AddEdge(v1, v2)
inputFile.close()

graph.SetColors()   # Setting colors for vertices
# print(graph.colors)
pairs = graph.FindPerfectMatching()   # Finding matching
# print(pairs)
resultMatrices = []
for pair in pairs:
    matrix = graph.CreateAdjMatrix()
    for i in range(len(matrix)):   
        for j in range(len(matrix)):
            if not matrix[i][j]:     # Where there are zeros, there is no edge, so it's a star
                matrix[i][j] = "*"

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1:   # Where there are ones, we make it zero to clear our matrix
                matrix[i][j] = "0"

    for u, v in pair:   # Then every pair places in matrix becoming ones
        matrix[u][v] = 1
        matrix[v][u] = 1
    resultMatrices.append(matrix)

for num, matrix in enumerate(resultMatrices): # Printing matrices
    print(f"Bipartite matching {num+1}")
    MatrixPrinter(matrix)
    print()
    
