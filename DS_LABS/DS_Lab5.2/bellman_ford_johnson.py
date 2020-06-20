from copy import deepcopy
# FUNCTIONS
def parse_file(text):
    result_list = []
    first_line = True
    for line in text:
        if first_line:
            nums = line.split()
            num_vert = int(nums[0])
            num_edge = int(nums[1])
            result_list.append([num_vert, num_edge])
            first_line = False
            continue
        nums = line.split()
        start = int(nums[0])
        end = int(nums[1])
        weight = int(nums[2])
        if [start, end, weight] not in result_list:
            result_list.append([start, end, weight])
    return result_list


def generate_marks(start_vertex, num_vertices):
    marks = {}
    for i in range(1, num_vertices + 1):
        if i == start_vertex:
            marks[i] = 0
            continue
        marks[i] = float('inf')
    return marks


def generate_routes(start_vertex, num_vertices):
    routes = {}
    for i in range(1, num_vertices + 1):
        if i == start_vertex:
            routes[i] = [start_vertex]
            continue
        routes[i] = None
    return routes


def make_dict(lst):
    d = dict()
    for i in range(1, lst[0][0] + 1):
        d[i] = []
        for j in range(1, len(lst)):
            if lst[j][0] == i and lst[j][1] not in d[i]:
                d[i].append([lst[j][1], lst[j][2]])
    return d


def sort_dict(di):
    for key in di:
        di[key].sort()
    return di


def dijkstra(graph, start_vertex):
    visited = []
    marks = generate_marks(start_vertex, len(graph))
    routes = generate_routes(start_vertex, len(graph))
    minval = marks[1]
    vert = 1
    while len(visited) < len(marks):
        for i in range(1, len(marks) + 1):
            if i not in visited:
                if marks[i] < minval:
                    minval = marks[i]
                    vert = i
        for adj in graph[vert]:
            if adj[0] not in visited:
                if marks[vert] + adj[1] < marks[adj[0]]:
                    routes[adj[0]] = list(routes[vert])
                    routes[adj[0]].append(adj[0])
                    marks[adj[0]] = marks[vert] + adj[1]
        minval = float('inf')
        visited.append(vert)
    return marks, routes


def bellman_ford(edgelist, start_vertex):
    marks = generate_marks(start_vertex, edgelist[0][0])
    routes = generate_routes(start_vertex, edgelist[0][0])
    for times in range(edgelist[0][0] - 1):
        for i in range(1, len(edgelist)):
            u = edgelist[i][0]
            v = edgelist[i][1]
            w = edgelist[i][2]
            if marks[v] > marks[u] + w:
                marks[v] = marks[u] + w
                routes[v] = list(routes[u])
                routes[v].append(v)
    for i in range(1, len(edgelist)):
        u = edgelist[i][0]
        v = edgelist[i][1]
        w = edgelist[i][2]
        if marks[v] > marks[u] + w:
            return "NC"
    return marks, routes


def add_vertex(edgelist):
    new_edgelist = deepcopy(edgelist)
    new_edgelist[0][0] += 1
    for j in range(1, edgelist[0][0] + 1):
        new_edgelist.append([new_edgelist[0][0], j, 0])
        new_edgelist[0][1] += 1
    return new_edgelist

def dict_to_list(dct):
    lst = []
    for k, v in dct.items():
        lst.append(v)
    return lst


def johnson(edgelist):
    # Step 1
    new_graph = add_vertex(edgelist)
    # Step 2
    start_johnson = new_graph[0][0]
    resu = bellman_ford(new_graph, start_johnson)
    if resu == "NC":
        print("Graph contain negative cycles\nAlgorithm is unable to work")
        return
    h = resu[0]
    # Step 3
    for i in range(1, len(new_graph)):
        u = new_graph[i][0]
        v = new_graph[i][1]
        new_graph[i][2] = new_graph[i][2] + h[u] - h[v]
    # Step 4
    dict_new_graph = make_dict(new_graph)
    sorted_new_graph = sort_dict(dict_new_graph)
    big_d_stroke = []
    all_routes = []
    for i in range(1, new_graph[0][0]):
        d = dijkstra(sorted_new_graph, i)
        marks = d[0]
        routes = d[1]
        lst = dict_to_list(marks)
        big_d_stroke.append(lst)
        all_routes.append(routes)
    # Step 5
    for i in range(len(big_d_stroke)):
        for j in range(len(big_d_stroke[i])):
            big_d_stroke[i][j] = big_d_stroke[i][j] - h[i + 1] + h[j + 1]
    # End of this nightmare
    return big_d_stroke, all_routes


# REAL MAINTAINING
def main():
    raw_text = open('input.txt')
    ordered_file = parse_file(raw_text)

    algo = input("Choose Bellman-Ford(b) or Johnson(j) algorithm: ")
    while algo != 'b' and algo != 'j':
        print("Try again")
        algo = input("Choose Bellman-Ford(b) or Johnson(j) algorithm: ")
    start_vertex = int(input("Enter your start vertex: "))
    type = int(input("Display:\n\
    Way to one vertex: 1\n\
    Way to all vertices: 2\n\
    Your choice: "))
    while type != 1 and type != 2:
        print("Try again")
        type = input("Display:\n\
        Way to one vertex: 1\n\
        Way to all vertices: 2\n\
        Your choice: ")
    if algo == 'b':
        res = bellman_ford(ordered_file, start_vertex)
        if res == "NC":
            print("Graph contains negative cycles\nAlgorithm is unable to work")
            return
        marks = res[0]
        routes = res[1]
        if type == 1:
            end_vertex = int(input("Enter your end vertex: "))
            print()
            print(f"Route:{routes[end_vertex]}")
            print(f"Route length: {marks[end_vertex]}")
        if type == 2:
            print()
            for el in routes:
                print(f"Route to vertex {el}: {routes[el]}\n\
Route length: {marks[el]}")
                print()
    if algo == 'j':
        res = johnson(ordered_file)
        if res is None:
            return
        big_d = res[0]
        routes = res[1]
        if type == 1:
            end_vertex = int(input("Enter your end vertex: "))
            print()
            print(f"Route: {routes[start_vertex - 1][end_vertex]}")
            print(f"Route length: {big_d[start_vertex - 1][end_vertex - 1]}")
        if type == 2:
            print()
            needed = routes[start_vertex - 1]
            for i in range(len(big_d)):
                print(f"Route to vertex {i + 1}: {needed[i + 1]}")
                print(f"Route length: {big_d[start_vertex - 1][i]}")
                print()
while input("Enter 'exit' to exit: ") != 'exit':
    main()
