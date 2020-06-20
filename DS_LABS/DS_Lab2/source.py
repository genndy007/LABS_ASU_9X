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

def parse_file(text):
    result_list = []
    for line in text:
        nums = line.split()
        start = int(nums[0])
        end = int(nums[1])
        if [start, end] not in result_list or [end, start] not in result_list:
            result_list.append([start, end])
    return result_list


def create_adj(source, graph_type):
    size = source[0][0]
    matrix = [[0 for i in range(size)] for j in range(size)]
    for k in range(1, len(source)):
        start = source[k][0]
        end = source[k][1]
        if graph_type == 'notdir':
            matrix[start - 1][end - 1] = 1
            matrix[end - 1][start - 1] = 1
        elif graph_type == 'dir':
            matrix[start - 1][end - 1] = 1
    return matrix


def multiply_matrix(matr1, matr2):
    size = len(matr1)
    result = [[0 for a in range(size)] for b in range(size)]

    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += matr1[i][k] * matr2[k][j]
    return result


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


def create_reach(matr_dist):
    size = len(matr_dist)
    matr_reach = [[1 for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            if matr_dist[i][j] == '∞':
                matr_reach[i][j] = 0
    return matr_reach


def find_eccens(matr_dist):
    size = len(matr_dist)
    eccens = []
    for i in range(size):
        ec = -1
        for j in range(size):
            if matr_dist[i][j] == "∞":
                ec = matr_dist[i][j]
                break
            elif matr_dist[i][j] > ec:
                ec = matr_dist[i][j]
        eccens.append(ec)
    return eccens

def find_radius(eccens):
    for el in eccens:
        el = str(el)
    return min(eccens)


def find_diameter(eccens):
    for el in eccens:
        el = str(el)
    return max(eccens)


def find_center(eccens, radius):
    centers = []
    for i in range(len(eccens)):
        if eccens[i] == radius:
            centers.append(i + 1)
    return centers


def find_tiers(matr_dist):
    result = []
    for i in range(len(matr_dist)):
        tiers = {}
        for j in range(len(matr_dist[i])):
            if tiers.get(matr_dist[i][j]) is None:
                tiers[matr_dist[i][j]] = [j + 1]
            else:
                tiers[matr_dist[i][j]].append(j + 1)
        result.append(tiers)
    return result


def check_silno(reach_matr):
    for i in range(len(reach_matr)):
        for j in range(len(reach_matr)):
            if reach_matr[i][j] == 0:
                return False
    return True


def check_odnob(reach_matr):
    for i in range(len(reach_matr)):
        for j in range(len(reach_matr)):
            if reach_matr[i][j] == 0 and reach_matr[j][i] == 0:
                return False
    return True


def check_slab(source):
    assoc = create_adj(source, 'notdir')
    dist_assoc = create_dist(assoc)
    reach_assoc = create_reach(dist_assoc)
    for i in range(len(reach_assoc)):
        for j in range(len(reach_assoc)):
            if reach_assoc[i][j] == 0:
                return False
    return True


def check_zvyaz(reach_matr, source):
    if check_silno(reach_matr):
        return 'Graph is silnozvyaz'
    elif check_odnob(reach_matr):
        return 'Graph is odnobzvyaz'
    elif check_slab(source):
        return 'Graph is slabkozvyaz'
    return 'Graph is nezvyaz'


def output_tiers(array):
    for i in range(len(array)):
        print(f"Tiers of vertex {i+1}:")
        for k, v in array[i].items():
            print(f"Distance {k}: Vertices:{v}//", end='')
        print()


def menu():
    handle = open('input.txt')
    source = parse_file(handle)
    while input("Type 'exit' to exit: ") != 'exit':
        graph = input('What graph (dir, notdir)?: ')

        matrix_adj = create_adj(source, graph)

        if graph == "notdir":
            wish = input("Enter:\n"
                         "1. Distance Matrix\n"
                         "2. Reach Matrix\n"
                         "3. Metrical Characteristics\n")
            dist_matrix = create_dist(matrix_adj)
            reach_matrix = create_reach(dist_matrix)
            if wish == '1':
                print("Distance matrix is:")
                out_matrix(dist_matrix)
                print()
            if wish == '2':
                print("Reach matrix is:")
                out_matrix(reach_matrix)
                print()
            if wish == '3':
                eccens = find_eccens(dist_matrix)
                radius = find_radius(eccens)
                diameter = find_diameter(eccens)
                centers = find_center(eccens, radius)
                tiers = find_tiers(dist_matrix)
                print("eccs:", eccens)
                print("R =", radius)
                print("D =", diameter)
                print("Centers are: ", centers)
                output_tiers(tiers)
        else:
            wish = input("Enter:\n"
                         "1. Distance Matrix\n"
                         "2. Reach Matrix\n"
                         "3. Connection Type\n")
            dist_matrix = create_dist(matrix_adj)
            reach_matrix = create_reach(dist_matrix)
            if wish == '1':
                print("Distance matrix is:")
                out_matrix(dist_matrix)
                print()
            if wish == '2':
                print("Reach matrix is:")
                out_matrix(reach_matrix)
                print()
            if wish == '3':
                print(check_zvyaz(reach_matrix, source))


if __name__ == '__main__':
    menu()
