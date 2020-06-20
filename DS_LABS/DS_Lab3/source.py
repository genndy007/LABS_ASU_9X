# queue and stack classes realization


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, number):
        self.queue.append(number)

    def dequeue(self):
        self.queue.pop(0)

    @property
    def length(self):
        return len(self.queue)

    @property
    def content(self):
        return self.queue

    @property
    def first(self):
        return self.queue[0]

    def print_content(self):
        if len(self.queue) == 0:
            print('Empty')
        else:
            for el in self.queue:
                print(f"{el}, ", end='')
            print()


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, number):
        self.stack.append(number)

    def pop(self):
        self.stack.pop() if len(self.stack) > 0 else print('Unable to pop')

    @property
    def top(self):
        return self.stack[-1] if len(self.stack) > 0 else print('No top number')

    @property
    def is_empty(self):
        return True if len(self.stack) == 0 else False

    @property
    def length(self):
        return len(self.stack)

    @property
    def content(self):
        return self.stack

    def print_content(self):
        if len(self.stack) == 0:
            print('Empty')
        else:
            for el in self.stack:
                print(f"{el}, ", end='')
            print()


# other functions to complete assignment


def parse_file(text):
    result_list = []
    for line in text:
        nums = line.split()
        start = int(nums[0])
        end = int(nums[1])
        if [start, end] not in result_list or [end, start] not in result_list:
            result_list.append([start, end])
    return result_list


def BFS_adequate(start, di):
    visited = [start]
    queue = Queue()
    queue.enqueue(start)
    BFS_nums = {start: 1}
    k = 1
    print(f"{start}       |  1    |    [{start}]") 
    while queue.length != 0:
        v = queue.first
        for i in range(len(di[v])):
            if di[v][i] not in visited:
                k += 1
                BFS_nums[di[v][i]] = k
                visited.append(di[v][i])
                queue.enqueue(di[v][i])
                print_status(di[v][i], k, queue.content)
            if i == len(di[v]) - 1:
                queue.dequeue()
                print(f"-       |  -    |    {queue.content}")


def DFS_adequate(start, di):
    visited = [start]
    stack = Stack()
    stack.push(start)
    DFS_num = {start:1}
    k = 1
    print(f"{start}       |  1    |    [{start}]")
    while not stack.is_empty:
        v = stack.top
        for i in range(len(di[v])):
            if di[v][i] not in visited:
                k += 1
                visited.append(di[v][i])
                DFS_num[di[v][i]] = k
                stack.push(di[v][i])
                print_status(di[v][i], k, stack.content)
                break
            elif i == len(di[v]) - 1:
                stack.pop()
                print(f"-       |  -    |    {stack.content}")



def print_status(vertex, BFS, queue):
    print(f"{vertex}       |  {BFS}    |    {queue}")


def make_dict(array, num_vert):
    d = dict()
    for i in range(1, num_vert + 1):
        d[i] = []
        for j in range(1, len(array)):
            if array[j][0] == i and array[j][1] not in d[i]:
                d[i].append(array[j][1])
            elif array[j][1] == i and array[j][0] not in d[i]:
                d[i].append(array[j][0])
    return d


def sort_dict(di):
    for key in di:
        di[key].sort()
    return di


def menu():
    handle = open('input.txt')
    comf = parse_file(handle)
    di = make_dict(comf, comf[0][0])
    di = sort_dict(di)

    while input("Type 'exit' to exit or press any key... ") != 'exit':
        start_vertex = int(input("Enter your start vertex: "))
        algorithm = input("What algorithm do you want (DFS/BFS)? ")
        while algorithm != "BFS" and algorithm != "DFS":
            print("Try again")
            algorithm = input("What algorithm do you want (DFS/BFS)? ")
        if algorithm == "BFS":
            print("Vertex  |BFS-num|  Queue")
            BFS_adequate(start_vertex, di)
        elif algorithm == "DFS":
            print("Vertex  |DFS-num|  Stack")
            DFS_adequate(start_vertex, di)

menu()