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


def create_undirected(dct):
    for key in dct:
        for el in dct[key]:
            if key in dct[el]:
                pass



########## REAL TESTING
handle = open('input.txt')
comf = parse_file(handle)
print(comf)
di = make_dict(comf, comf[0][0])
di = sort_dict(di)
print(di)
# undir = create_undirected(di)
