import time
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


def floyd_warshall(matrix):
    history = create_history_matrix(len(matrix))

    for k in range(len(matrix)):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                    history[i][j] = history[k][j]
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
                if matrix[i][i] < 0:
                    print("There is a negative cycle")

    return matrix, history

def find_route(hist, start, end):
    route = [end]
    piece = hist[start - 1][end - 1]
    route.insert(0, piece)
    while piece != start:
        piece = hist[start - 1][piece - 1]
        route.insert(0, piece)
    return route

# PENTEST
text = open('input.txt')
parsed = parse_file(text)
start_matrix = create_start_matrix(parsed)

print("Start matrix W^(0)")
out_matrix(start_matrix)
print()
time.sleep(1)
result = floyd_warshall(start_matrix)
matrix = result[0]
history = result[1]
route = find_route(history, 1, 4)
print("Route between 3 and 2 is", route)
print("After floyd warshall")
out_matrix(matrix)
