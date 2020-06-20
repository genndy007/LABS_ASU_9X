def parse_file(text):
    result_list = []
    for line in text:
        nums = line.split()
        start = int(nums[0])
        end = int(nums[1])
        result_list.append([start, end])
    return result_list


def make_dict(lst):
    d = dict()
    for i in range(1, lst[0][0] + 1):
        d[i] = []
        for j in range(1, len(lst)):
            if lst[j][0] == i and lst[j][1] not in d[i]:
                d[i].append(lst[j][1])
            if lst[j][1] == i and lst[j][0] not in d[i]:
                d[i].append(lst[j][0])
    return d


def sort_dict(di):
    for key in di:
        di[key].sort()
    return di

def check_euler_cycle(dct):
    for i in range(1, len(dct) + 1):
        if len(dct[i]) % 2 != 0:
            return False
    return True

def check_euler_route(dct):
    num_odd = 0
    for i in range(1, len(dct) + 1):
        if len(dct[i]) % 2 != 0:
            num_odd += 1
    if num_odd == 2:
        return True
    return False

def processing_edgelist(graph_list):
    edgelist = list(graph_list)
    edgelist.pop(0)
    reversed = []
    for i in range(len(edgelist)):
        reversed.append([edgelist[i][1], edgelist[i][0]])
    for el in reversed:
        edgelist.append(el)
    edgelist.sort()
    return edgelist

def euler_cycle(edgelist):
    curr = 1
    vis_edges = []
    cycle = []
    while len(vis_edges) < len(edgelist):
        for i in range(len(edgelist)):
            if edgelist[i][0] == curr and [edgelist[i][0], edgelist[i][1]] not in vis_edges:
                cycle.append(edgelist[i])
                vis_edges.append([edgelist[i][0], edgelist[i][1]])
                vis_edges.append([edgelist[i][1], edgelist[i][0]])
    return cycle


##### TESTING
raw = open('input.txt')
parsed = parse_file(raw)
d = make_dict(parsed)
d = sort_dict(d)
print(parsed)
print(d)
print(check_euler_cycle(d))
edgelist = processing_edgelist(parsed)
print(edgelist)
ec = euler_cycle(edgelist)
print(ec)
