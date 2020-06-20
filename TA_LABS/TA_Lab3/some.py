class IndexUnit:
    def __init__(self, key, index):
        self.key = key
        self.index = index

class MainUnit:
    def __init__(self, index, value):
        self.index = index
        self.value = value

index_file = []
main_file = []

print("Set of commands: ADD, FIND")
index = 0
while input("Type 'exit' to exit: ") != 'exit':
    command = input('>>> ')
    lst = command.split()
    if lst[0] == "ADD":
        index_file.append(IndexUnit(lst[1], index))
        main_file.append(MainUnit(index, lst[2]))
        index += 1

print("Here is index file content")
for unit in index_file:
    print(unit.key, unit.index)

print("here is main file content")
for unit in main_file:
    print(unit.index, unit.value)






