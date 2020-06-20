# Needed for testing and printing those matrices
def out_matrix(matr):
    print('    ', end='')
    for i in range(len(matr)):
        print(f"v{i+1}  ", end='')
    print()
    for i in range(len(matr)):
        print(f"v{i+1}", end='')
        for j in range(len(matr[i])):
            print(f"   {matr[i][j]}", end='')
        print()

# Parse file into list to work
def parse_file(text):
    result_list = []
    for line in text:
        nums = line.split()
        start = int(nums[0])
        end = int(nums[1])
        if [start, end] not in result_list or [end, start] not in result_list:
            result_list.append([start, end])
    return result_list

# Creating adjacency and distance matrices to be able to create reach matrix
def create_adj(source):
    size = source[0][0]
    matrix = [[0 for i in range(size)] for j in range(size)]
    for k in range(1, len(source)):
        start = source[k][0]
        end = source[k][1]
        matrix[start - 1][end - 1] = 1
    return matrix

# Matrix multiplication is also needed in process of creating distance matrix
def multiply_matrix(matr1, matr2):
    size = len(matr1)
    result = [[0 for a in range(size)] for b in range(size)]

    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += matr1[i][k] * matr2[k][j]
    return result

# Creating distance matrix
def create_dist(matr_adj):
    size = len(matr_adj)
    first_matr_adj = matr_adj
    matr_dist = matr_adj
    overcame = [(i, i) for i in range(size)]
    for i in range(size):
        for j in range(size):
            if matr_dist[i][j] != 0 and (i, j) not in overcame:
                overcame.append((i, j))
    times = 1
    while times <= size - 1:
        times += 1
        matr_adj = multiply_matrix(matr_adj, first_matr_adj)
        for i in range(size):
            for j in range(size):
                if matr_adj[i][j] != 0 and (i, j) not in overcame:
                    matr_dist[i][j] = times
                    overcame.append((i, j))
    for i in range(size):
        for j in range(size):
            if matr_dist[i][j] == 0 and (i, j) not in overcame:
                matr_dist[i][j] = "∞"
    return matr_dist

# Make a dictionary to work
def make_dict(array, num_vert):
    d = dict()
    for i in range(1, num_vert + 1):
        d[i] = []
        for j in range(len(array)):
            if array[j][0] == i and array[j][1] not in d[i]:
                d[i].append(array[j][1])
            if array[j][1] == i and array[j][0] not in d[i]:
                d[i].append(array[j][0])
    return d

# Sort dictionary elements
def sort_dict(di):
    for key in di:
        di[key].sort()
    return di

# BFS realization: made it easier because we only need visited vertices
def BFS_simplified(start, di):
    visited = [start]
    queue = []
    queue.append(start)
    while len(queue) != 0:
        v = queue[0]
        if len(di[v]) == 0:
            return visited
        for i in range(len(di[v])):
            if di[v][i] not in visited:
                visited.append(di[v][i])
                queue.append(di[v][i])
            if i == len(di[v]) - 1:
                queue.pop(0)
    return visited

# Step 1: Creating reach matrix
def create_reach(matr_dist):
    size = len(matr_dist)
    matr_reach = [[1 for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            if matr_dist[i][j] == '∞':
                matr_reach[i][j] = 0
    return matr_reach

# Step 2: Creating an undirected graph using reach matrix
def create_undir(reach):
    undir_graph = []
    for i in range(len(reach)):
        for j in range(len(reach[i])):
            if reach[i][j] == reach[j][i] == 1 and i != j:
                if [i+1, j+1] not in undir_graph and [j+1, i+1] not in undir_graph:
                    undir_graph.append([i + 1, j + 1])
    return undir_graph

# Step 3: Find connected components in undirected graph, it is easier :)
def find_conn_comps(dct):
    visited = []
    comps = []
    for k, v in dct.items():
        if k not in visited:
            one_time_vis = BFS_simplified(k, dct)
            for el in one_time_vis:
                visited.append(el)
            comps.append(one_time_vis)
    return comps


### TESTING
# Step 1
raw = open('input.txt')
parsed = parse_file(raw)
matr_adj = create_adj(parsed)
matr_dist = create_dist(matr_adj)
matr_reach = create_reach(matr_dist)
print("Reach matrix:")
out_matrix(matr_reach)
print()

# Step 2
undir_graph = create_undir(matr_reach)
num_verts = len(matr_reach)
dct = make_dict(undir_graph, num_verts)
srt = sort_dict(dct)

# Step 3
result = find_conn_comps(srt)

# Output our results
print("Found those strong connection components:")
for el in result:
    print(el)
print(f"Number of them: {len(result)}")
