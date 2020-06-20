######### FUNCTIONS #########


def parse_file(text):
    result_list = []
    for line in text:
        nums = line.split()
        start = int(nums[0])
        end = int(nums[1])
        if [start, end] not in result_list or [end, start] not in result_list:
            result_list.append([start, end])
    return result_list


def make_dict(array, num_vert):
    d = dict()
    for i in range(1, num_vert + 1):
        d[i] = []
        for j in range(1, len(array)):
            if array[j][0] == i and array[j][1] not in d[i]:
                d[i].append(array[j][1])
    return d


def sort_dict(di):
    for key in di:
        di[key].sort()
    return di

def all_in_visited(list1, list2):
    for element in list1:
        if element not in list2:
            return False
    return True

def make_top_look_adequate(top):
    result_list = []
    for k, v in top.items():
        result_list.insert(0, k)
    return result_list

######## LABA KONKRETNO
def my_DFSR(dictionary, start, visited=[], ordering=[]):
    visited.append(start)
    if all_in_visited(dictionary[start], visited):
        ordering.insert(0, start)
        return visited, ordering
    for el in dictionary[start]:
        if el not in visited:
            visited, ordering = my_DFSR(dictionary, el, visited, ordering)
    return visited, ordering


def DFSR(dictionary, start, label=0, topolog_num = {}, visited=[]):
    visited.append(start)
    # print(f"Vertex: {start}, DFS-num: {k}")
    for i in range(len(dictionary[start])):
        if dictionary[start][i] not in visited:
            DFSR(dictionary, dictionary[start][i], label - 1, topolog_num, visited)
    topolog_num[start] = label
    label -= 1


def TopologicalSort_DFSR(dictionary):
    current_label = len(dictionary)
    topolog_num = {}
    visited = []
    for i in range(1, len(dictionary) + 1):
        if i not in visited:
            some_result = DFSR(dictionary, i, current_label)

def topsort(dictionary):
    n = len(dictionary)
    visited_all = [False for i in range(n)]
    ordering = [0 for i in range(n)]
    i = n - 1    # index for ordering

    for at in range(n):
        if not visited_all[at]:
            visited_nodes = []
            DFS()
            for node_id in visited_nodes:
                ordering[i] = node_id
                i = i - 1
    return ordering


def TopologicalSort(dictionary):
    visited = []
    ordering = {}
    current_label = len(dictionary)
    for vertex in dictionary:
        if vertex not in visited:
            ordering, visited, current_label = DFSRecur(dictionary,
            vertex, visited, ordering, current_label)
    return ordering

def DFSRecur(dictionary, vertex, visited, ordering, current_label):
    visited.append(vertex)
    for u in dictionary[vertex]:
        if u not in visited:
            ordering, visited, current_label = DFSRecur(dictionary,
            u, visited, ordering, current_label)
    ordering[vertex] = current_label
    current_label -= 1
    return ordering, visited, current_label

###### TESTING ##############

handle = open('input.txt')
comf = parse_file(handle)

di = make_dict(comf, comf[0][0])
di = sort_dict(di)

top_sort = TopologicalSort(di)

actual_result = make_top_look_adequate(top_sort)
print("The topological sort order:", actual_result)
