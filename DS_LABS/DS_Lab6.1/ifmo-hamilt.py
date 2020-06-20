from copy import deepcopy
def parse_file(text):
    graph = []
    for line in text:
        nums = line.split()
        graph.append([int(nums[0]), int(nums[1])])
    return graph

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

def DiracTheorem(graph):
    degrees = FindDegree(graph)
    print(degrees)
    for key in degrees:
        if degrees[key] < len(degrees)/2:
            return False
    return True


def create_list_for_hamilton(lst):
    ham_list = []
    for i in range(1, len(lst)):
        v1 = lst[i][0]
        v2 = lst[i][1]
        ham_list.append([v1, v2])
        ham_list.append([v2, v1])
    return ham_list

def FindHamiltonianCycle(right_list, num_vert):
    queue = [i for i in range(1, num_vert+1)]
    for k in range(num_vert*(num_vert - 1)):
        if [queue[0], queue[1]] not in right_list:
            i = 2
            while [queue[0], queue[i]] not in right_list or [queue[1], queue[i+1]] not in right_list:
                i += 1
            j = 0
            while 1 + j < i - j:
                 queue[1 + j], queue[i - j] = queue[i - j], queue[1 + j]
                 j += 1
        queue.append(queue[0])
        queue.pop(0)
    return queue



####### TEST
raw = open('super.txt')
graph = parse_file(raw)
check_dirac = DiracTheorem(graph)
print(check_dirac)
hamilton_list = create_list_for_hamilton(graph)
cycle = FindHamiltonianCycle(hamilton_list, graph[0][0])
print(cycle)


