############# AUXILIARY FUNCTIONS

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


def make_top_look_adequate(top):
    result_list = []
    for k, v in top.items():
        result_list.insert(0, k)
    return result_list

######## TOPOLOGICAL SORT REALIZATION
def topological_sort(dictionary):
    visited = []
    ordering = {}
    current_label = len(dictionary)
    for vertex in dictionary:
        if vertex not in visited:
            ordering, visited, current_label = DFS_Recur(dictionary,
            vertex, visited, ordering, current_label)
    return ordering

def DFS_Recur(dictionary, vertex, visited, ordering, current_label):
    visited.append(vertex)
    for u in dictionary[vertex]:
        if u not in visited:
            ordering, visited, current_label = DFS_Recur(dictionary,
            u, visited, ordering, current_label)
    ordering[vertex] = current_label
    current_label -= 1
    return ordering, visited, current_label

########## REAL TESTING
handle = open('input.txt')
comf = parse_file(handle)

di = make_dict(comf, comf[0][0])
di = sort_dict(di)

top_sort = topological_sort(di)

actual_result = make_top_look_adequate(top_sort)
print("The topological sort order:", actual_result)
