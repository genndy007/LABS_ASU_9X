from copy import deepcopy
# file parsing
def ParseFile(text):
    graph = []
    for line in text:
        nums = line.split()
        graph.append([int(nums[0]), int(nums[1])])
    return graph
#-------------

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
# for Euler path and cycle
def FindEulerPath(graph):
    path = []
    stack = [1]    # Creating stack and putting vertex into it
    while len(stack) > 0:  # while stack is not empty
        degree = FindDegree(graph)  # Check vertices degrees
        v = stack[-1]   # v is top stack element
        if degree[v] == 0:  # if v degree is 0
            path.append(v)  # add to resulting path
            stack.pop()    # delete out of stack
        else:
            for i in range(1, len(graph)): # Searching through graph
                if v in graph[i]:   # Find edge that comes to v
                    if graph[i][0] == v:
                        stack.append(graph[i][1])  # put it to stack
                    elif graph[i][1] == v:
                        stack.append(graph[i][0])
                    graph.pop(i)  # Delete this edge
                    break
    return path


def CheckEulerCycle(graph):  # If there is only even degrees
    degrees = FindDegree(graph)
    for key in degrees:
        if degrees[key] % 2 != 0:
            return False
    return True

def CheckEulerPath(graph):  # If there is only 2 odd degrees
    degrees = FindDegree(graph)
    odd = 0
    for key in degrees:
        if degrees[key] % 2 != 0:
            odd += 1
    if odd == 2:
        return True
    return False
#-----------------

# check Dirac Theorem
def DiracTheorem(graph):  # Every vertex degree should have
    degrees = FindDegree(graph) # degree more than n/2
    for key in degrees:     # Not mandatory but enough for being
        if degrees[key] < len(degrees)/2: # Hamiltonian 
            return False
    return True
#------------------
# for Hamilton cycle and path
def CreateListForHamilton(lst):
    ham_list = []
    for i in range(1, len(lst)):   # Making graph easier to process
        v1 = lst[i][0]
        v2 = lst[i][1]
        ham_list.append([v1, v2])
        ham_list.append([v2, v1])
    return ham_list

def FindHamiltonianCycle(graph):
    hamilton_list = CreateListForHamilton(graph)
    num_vert = graph[0][0]
    queue = [i for i in range(1, num_vert+1)]  # Initializing the queue
    for k in range(num_vert*(num_vert - 1)):  # Performing n*(n-1) times
        if [queue[0], queue[1]] not in hamilton_list:  # If there is an edge between first two verts of queue
            i = 2
            while [queue[0], queue[i]] not in hamilton_list or [queue[1], queue[i+1]] not in hamilton_list:
                i += 1    # Finding index satisfying our needs 
            j = 0
            while 1 + j < i - j:  # Swapping subqueue for guaranteeing that edge exists between verts
                 queue[1 + j], queue[i - j] = queue[i - j], queue[1 + j]
                 j += 1
        queue.append(queue[0])  # Then place first vertex
        queue.pop(0)            # to the end of queue
    return queue
#--------------

# infinite cycle

while input("Type 'exit' to exit: ") != 'exit':
    algo = input("Choose cycles you want - Euler(e) or Hamilton(h): ")
    while algo != 'e' and algo != 'h':
        algo = input("Choose cycles you want - Euler(e) or Hamilton(h): ")

    raw = open('input.txt')
    graph = ParseFile(raw)
    if algo == 'e':
        if CheckEulerCycle(graph):
            print("There is Euler cycle:")
        elif CheckEulerPath(graph):
            print("There is Euler path:")
        if CheckEulerCycle(graph) or CheckEulerPath(graph):
            euler_graph = deepcopy(graph)
            path = FindEulerPath(euler_graph)
            print(path)
        else:
            print("There is no Euler cycle or path")

    if algo == 'h':
        check_dirac = DiracTheorem(graph)
        print('Dirac theorem runs here:', check_dirac)
        cycle = FindHamiltonianCycle(graph)
        if [cycle[0], cycle[-1]] in graph or [cycle[-1], cycle[0]] in graph:
            print('Here is Hamilton cycle')
        else:
            print('Here is Hamilton path')
        print('Found:', cycle)