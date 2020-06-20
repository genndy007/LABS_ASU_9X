
# UBER SUPER FUNCTIONS
def parse_d(text):
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
        if weight < 0:
            return None
    return result_list


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


def dijkstra(graph, start):
    visited = []
    marks = generate_marks(start_vertex, ordered_file[0][0])
    routes = generate_routes(start_vertex, ordered_file[0][0])
    #print(routes)
    minval = marks[1]
    vert = 1
    while len(visited) < len(marks):
        for i in range(1, len(marks) + 1):
            if i not in visited:
                if marks[i] < minval:
                    minval = marks[i]
                    vert = i
        #print(f"Going on vertex {vert} with minval {minval}")
        for adj in graph[vert]:
            if adj[0] not in visited:
                if marks[vert] + adj[1] < marks[adj[0]]:
                    routes[adj[0]] = list(routes[vert])
                    routes[adj[0]].append(adj[0])
                    #print(routes[adj[0]])

                    marks[adj[0]] = marks[vert] + adj[1]
                    #print(f"Now {adj[0]} mark is {marks[adj[0]]}")
        minval = float('inf')
        visited.append(vert)
        # print(f"Visited are:{visited}")
        # print(f"Routes are: {routes}")
    return marks, routes


# PENETRATION TESTING
raw_text = open('input.txt')
ordered_file = parse_d(raw_text)
dicted_file = make_dict(ordered_file)
sorted_file = sort_dict(dicted_file)

start_vertex = int(input("Enter start vertex: "))
end_vertex = int(input("Enter vertex you need way to: "))
# marks = generate_marks(start_vertex, ordered_file[0][0])
algo = dijkstra(sorted_file)
marks = algo[0]
routes = algo[1]
print(marks)
print(routes)
print(f"The route from vertex {start_vertex} to vertex {end_vertex}\n\
lies on vertices {routes[end_vertex]}")
print(f"The length of the route is {marks[end_vertex]}")
