def MatrixPrinter(matrix):
    numVert = len(matrix)
    print("   ", end='')
    for i in range(numVert):
        print(f"{i+1} ", end='')
    print()
    for i in range(numVert):
        print(f'{i+1} ', *matrix[i])


def Conveyor():
    s = '*'
    return [[s,s,s,0,0,s], [s,s,s,s,0,0], [s,s,s,0,0,0], [0,s,0,s,s,s], [0,0,0,s,s,s], [s,0,0,s,s,s]]

match1 = Conveyor()
match1[0][3] = 1
match1[3][0] = 1

match1[1][4] = 1
match1[4][1] = 1

match1[2][5] = 1
match1[5][2] = 1
print("Bipartite matching 1")
MatrixPrinter(match1)

match2 = Conveyor()
match2[0][3] = 1
match2[3][0] = 1

match2[1][5] = 1
match2[5][1] = 1

match2[2][4] = 1
match2[4][2] = 1
print("Bipartite matching 2")
MatrixPrinter(match2)

match3 = Conveyor()
match3[0][4] = 1
match3[4][0] = 1

match3[1][5] = 1
match3[5][1] = 1

match3[2][3] = 1
match3[3][2] = 1
print("Bipartite matching 3")
MatrixPrinter(match3)