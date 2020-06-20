from itertools import permutations  # Перестановки


def DistanceBetweenPoints(point1, point2): # Function for finding distance
    x1, y1, n1 = point1                    # between 2 points with school
    x2, y2, n2 = point2                    # formula
    dist = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return dist



class GraphOnPlane:
    def __init__(self, numVert):
        self.numVert = numVert
        self.adjCostMatrix = [[0.0 for i in range(self.numVert)] for i in range(self.numVert)]
        

    def TravellingSalesmanProblem(self):
        minimalPermutation = None    # starting values for min-perm and
        minimalCost = float('inf')   # min-cost

        for permutation in permutations(tuple(range(self.numVert))):   # Checking every permutation
            perm = list(permutation)
            cost = 0
            
            while len(perm) != 1:
                v1 = perm.pop(0)   # Summing the distance of chosen way
                v2 = perm[0]
                cost += self.adjCostMatrix[v1][v2]

            start = permutation[-1]   
            end = permutation[0] 
            cost += self.adjCostMatrix[start][end]   # Adding final edge of coming back to start

            if cost < minimalCost:  # If this way is better so this becomes the best way
                minimalPermutation = permutation
                minimalCost = cost

        return minimalCost, minimalPermutation


def ResultsPrinter(perm, cost):      # Good printer
    print('Shortest way algorithm found:')
    for vertex in perm:
        print(vertex + 1, ' -> ', end='')
    print(perm[0] + 1)

    print(f"Cost of the route: {round(cost, 1)}")

file = open('input.txt')   
numVert = int(file.readline())    # Getting vertex numbers

coordinates = []

for num, line in enumerate(file):     # Managing points coordinates
    point = line.split()
    for i in range(len(point)):
        point[i] = int(point[i])
    coordinates.append(tuple([point[0], point[1], num]))

graph = GraphOnPlane(numVert)

for point1 in coordinates:    # Filling adjacency cost matrix 
    for point2 in coordinates:
        graph.adjCostMatrix[point1[2]][point2[2]] = DistanceBetweenPoints(point1, point2)
        graph.adjCostMatrix[point2[2]][point1[2]] = DistanceBetweenPoints(point1, point2) 

cost, perm = graph.TravellingSalesmanProblem()

ResultsPrinter(perm, cost)
