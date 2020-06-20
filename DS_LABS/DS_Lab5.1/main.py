######### DIJKSTRA
# Parsing file
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

# Creating and sorting dictionaries for work convenience
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

# Generating basic marks and routes for start
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

# Dijkstra itself
def dijkstra(graph, start, file):
    visited = []
    marks = generate_marks(start, file[0][0])
    routes = generate_routes(start, file[0][0])
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

######## FLOYD-WARSHALL
# Parse file
def parse_f(text):
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

# Printing matrices
def out_matrix(matrix):
    print("  ", end='')
    for k in range(len(matrix)):
        print(f" v{k+1} ", end='')
    print()
    for i in range(len(matrix)):
        print(f"v{i+1}", end='  ')
        for j in range(len(matrix[i])):
            el = matrix[i][j] if matrix[i][j] != float('inf') else u'\u221e'
            print(el, end='  ')
        print()

# Creating basic matrices for distance matrix and history matrix
def create_start_matrix(cond):
    matrix = [[float('inf') for i in range(cond[0][0])] for i in range(cond[0][0])]
    for i in range(cond[0][0]):
        matrix[i][i] = 0
    for i in range(1, len(cond)):
        matrix[cond[i][0] - 1][cond[i][1] - 1] = cond[i][2]
    return matrix

def create_history_matrix(size):
    matrix = [[0 for i in range(size)] for i in range(size)]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = i + 1
    for i in range(len(matrix)):
        matrix[i][i] = 0
    return matrix

# Floyd-Warshall itself
def floyd_warshall(matrix):
    history = create_history_matrix(len(matrix))

    for k in range(len(matrix)):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                    history[i][j] = history[k][j]
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
                if matrix[i][i] < 0:
                    return None

    return matrix, history

# Finding route from history matrix
def find_route(hist, start, end):
    route = [end]
    piece = hist[start - 1][end - 1]
    route.insert(0, piece)
    while piece != start:
        piece = hist[start - 1][piece - 1]
        route.insert(0, piece)
    return route

# Managing output to the file
def output_to_file(matrix, filename):
    with open(filename, 'w') as f:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                f.write(f"{matrix[i][j]} ")
            f.write("\n")


# Main menu
def main():
    algo = input("Choose Dijkstra(d) or Floyd-Warshall(f): ")
    while algo != 'd' and algo != 'f':
        print("Try again")
        algo = input("Choose Dijkstra(d) or Floyd-Warshall(f)")

    raw_text = open('input.txt')
    if algo == 'd':
        parsed = parse_d(raw_text)
        if parsed is None:
            print("Found a negative weight, terminating...")
            return
        dicted_file = make_dict(parsed)
        sorted_file = sort_dict(dicted_file)

        start_vertex = int(input("Enter start vertex: "))
        type = int(input("Find way to one vertex - 1\nFind way to all vertices - 2\n"))
        while type != 1 and type != 2:
            type = int(input("Find way to one vertex - 1\n Find way to all vertices - 2\n"))

        result = dijkstra(sorted_file, start_vertex, parsed)
        if type == 1:
            end_vertex = int(input("Enter end vertex:"))
            marks = result[0]
            routes = result[1]
            print(f"The route from vertex {start_vertex} to vertex {end_vertex}\n\
            lies on vertices {routes[end_vertex]}")
            print(f"The length of the route is {marks[end_vertex]}")
        if type == 2:
            marks = result[0]
            routes = result[1]
            for i in range(1, len(marks) + 1):
                print(f"Route from {start_vertex} to {i}: {routes[i]}")
                print(f"It's length: {marks[i]}")
    if algo == 'f':
        parsed = parse_f(raw_text)
        start_matrix = create_start_matrix(parsed)
        result = floyd_warshall(start_matrix)
        if result is None:
            print("Found a negative cycle, terminating...")
            return
        matrix = result[0]
        history = result[1]
        print(f"W^({len(matrix)})")
        out_matrix(matrix)
        print(f"Theta^({len(matrix)})")
        out_matrix(history)
        wish = input("Do you want route?(y/n): ")
        if wish == 'y':
             start_vertex = int(input("Enter start vertex: "))
             end_vertex = int(input("Enter end vertex: "))
             route = find_route(history, start_vertex, end_vertex)
             print(f"Route between {start_vertex} and {end_vertex}: {route}")
             print(f"It's length: {matrix[start_vertex - 1][end_vertex - 1]}")
        tofile = input("Want to output matrices to file?(y/n): ")
        if tofile == 'y':
            output_to_file(matrix, 'dist.txt')
            output_to_file(history, 'hist.txt')

while input("Enter 'exit' to exit or press any key... ") != 'exit':
    main()
