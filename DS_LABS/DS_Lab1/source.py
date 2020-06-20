def out_matrix(matr, matr_type):
    print("     ", end='')
    for k in range(len(matr[0])):
        if matr_type == 'inc':
            print("e{}  ".format(k + 1), end='')
        elif matr_type == 'adj':
            print("v{}  ".format(k + 1), end='')
    print()
    for i in range(len(matr)):
        print("v{}".format(i + 1), end='')
        for j in range(len(matr[i])):
            print("{:4d}".format(matr[i][j]), end='')
        print()


def create_inc(source, graph_type):
    rows = source[0][0]
    cols = source[0][1]
    matrix = [[0 for i in range(cols)] for j in range(rows)]
    for k in range(1, len(source)):
        start = source[k][0]
        end = source[k][1]
        if graph_type == 'notdirected':
            matrix[start - 1][k - 1] = 1
            matrix[end - 1][k - 1] = 1
        elif graph_type == 'directed':
            if start == end:
                matrix[start - 1][k - 1] = 2
            else:
                matrix[start - 1][k - 1] = -1
                matrix[end - 1][k - 1] = 1
    return matrix


def create_adj(source, graph_type):
    size = source[0][0]
    matrix = [[0 for i in range(size)] for j in range(size)]
    for k in range(1, len(source)):
        start = source[k][0]
        end = source[k][1]
        if graph_type == 'notdirected':
            matrix[start - 1][end - 1] = 1
            matrix[end - 1][start - 1] = 1
        elif graph_type == 'directed':
            matrix[start - 1][end - 1] = 1
    return matrix

def find_degree(source):
    vertices = source[0][0]
    degree_list = [0 for i in range(vertices)]
    for k in range(1, len(source)):
        ver1 = source[k][0]
        ver2 = source[k][1]
        degree_list[ver1 - 1] += 1
        degree_list[ver2 - 1] += 1
    return degree_list

def is_regular(lst):
    checker = lst[0]
    for el in lst:
        if checker != el:
            return False
    return True

def isolated_hanging_vert(lst):
    hanging = []
    isolated = []
    for i in range(len(lst)):
        if lst[i] == 0:
            isolated.append(i + 1)
        if lst[i] == 1:
            hanging.append(i + 1)
    return isolated, hanging


def list_printer(lst):
    for el in lst:
        print("{}, ".format(el), end='')

def find_half_degrees(source):
    vertices = source[0][0]
    in_outs = [[0, 0] for i in range(vertices)]
    for k in range(1, len(source)):
        start = source[k][0]
        end = source[k][1]
        in_outs[start - 1][1] += 1
        in_outs[end - 1][0] += 1
    return in_outs

def half_degrees_printer(lst):
    for i in range(len(lst)):
        print(i + 1, "vertex ins and outs", lst[i][0], ',', lst[i][1])


def parse_file(text):
    result_list = []
    for line in text:
        nums = line.split()
        start = int(nums[0])
        end = int(nums[1])
        if [start, end] not in result_list or [end, start] not in result_list:
            result_list.append([start, end])
    return result_list

def directed_graph(file):
    print("1. Incidence matrix")
    print("2. Adjacency matrix")
    print("3. In/out-degrees")
    user_choice = 0
    while user_choice < 1 or user_choice > 3:
        user_choice = int(input("What do you need? (1-3) "))
    if user_choice == 1:
        matrix_inc = create_inc(file, 'directed')
        print("Incidence matrix from orient.txt is: ")
        out_matrix(matrix_inc, 'inc')
    if user_choice == 2:
        matrix_adj = create_adj(file, 'directed')
        print("Adjacency matrix from orient.txt is: ")
        out_matrix(matrix_adj, 'adj')
    if user_choice == 3:
        print("Ins and outs of graph: ")
        half_degrees = find_half_degrees(file)
        half_degrees_printer(half_degrees)


def notdirected_graph(file):
    print("1. Incidence matrix")
    print("2. Adjacency matrix")
    print("3. Vertices degrees and check regularity")
    print("4. Find isolated and hanging vertices")
    degree_list = find_degree(file)
    user_choice = 0
    while user_choice < 1 or user_choice > 4:
        user_choice = int(input("What do you need? (1-4) "))
    if user_choice == 1:
        matrix_inc = create_inc(file, 'notdirected')
        print("Incidence matrix from notorient.txt is: ")
        out_matrix(matrix_inc, 'inc')
    if user_choice == 2:
        matrix_adj = create_adj(file, 'notdirected')
        print("Adjacency matrix from orient.txt is: ")
        out_matrix(matrix_adj, 'adj')
    if user_choice == 3:
        print('Degrees of vertices are: ')
        print(degree_list)
        print()
        regular = is_regular(degree_list)
        print("Is graph regular?")
        print(regular)
        print()
        if regular:
            print("Degree of regularity:", degree_list[0])
    if user_choice == 4:
        lst = isolated_hanging_vert(degree_list)
        isolated = lst[0]
        hanging = lst[1]
        print("Isolated vertices are: ", end='')
        list_printer(isolated)
        print()
        print("Hanging vertices are: ", end='')
        list_printer(hanging)


def menu():
    while True:
        graph_type = input("What is your graph type(directed or notdirected)?: ")
        if graph_type == "directed":
            notorient_file = "orient.txt"
            handle_notorient = open(notorient_file, 'r')
            comf = parse_file(handle_notorient)
            directed_graph(comf)
        elif graph_type == 'notdirected':
            orient_file = "notorient.txt"
            handle_orient = open(orient_file, 'r')
            comf2 = parse_file(handle_orient)
            notdirected_graph(comf2)
        print()
        if input("Type 'exit' to exit of press any key: ") == 'exit':
            break


menu()

