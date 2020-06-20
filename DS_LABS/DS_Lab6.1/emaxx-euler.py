from copy import deepcopy
def parse_file(text):
    graph = []
    for line in text:
        nums = line.split()
        graph.append([int(nums[0]), int(nums[1])])
    return graph

# def FindEulerPath(graph, v=1):
#     usedGraph = deepcopy(graph)
#     print(v)
#     while len(usedGraph) > 0:
#         for edge in usedGraph:
#             if edge[0] == v:
#                 v = edge[1]
#                 usedGraph.remove(edge)
#                 FindEulerPath(usedGraph, v)
#             elif edge[1] == v:
#                 v = edge[0]
#                 usedGraph.remove(edge)
#                 FindEulerPath(usedGraph, v)
def CreateDictForDegree(graph):
    dct = {}
    for i in range(1, graph[0][0]+1):
        dct[i] = 0
    return dct

def FindDegree(graph):
    degrees = CreateDictForDegree(graph)
    for i in range(1, len(graph)):
        degrees[graph[i][0]] += 1
        degrees[graph[i][1]] += 1
    return degrees


def FindEulerPath(graph):
    path = []
    stack = [1]
    while len(stack) > 0:
        degree = FindDegree(graph)
        v = stack[-1]
        if degree[v] == 0:
            path.append(v)
            stack.pop()
        else:
            for i in range(1, len(graph)):
                if v in graph[i]:
                    if graph[i][0] == v:
                        stack.append(graph[i][1])
                    elif graph[i][1] == v:
                        stack.append(graph[i][0])
                    graph.pop(i)
                    break
    return path


def CheckEulerCycle(graph):
    degrees = FindDegree(graph)
    for key in degrees:
        if degrees[key] % 2 != 0:
            return False
    return True

def CheckEulerPath(graph):
    degrees = FindDegree(graph)
    odd = 0
    for key in degrees:
        if degrees[key] % 2 != 0:
            odd += 1
    if odd == 2:
        return True
    return False


####### TEST
raw = open('input.txt')
graph = parse_file(raw)
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
# print(euler_graph)
# print(graph)

# FindEulerPath(graph)

