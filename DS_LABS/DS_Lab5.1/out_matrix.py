from random import randint
matrix = [[randint(0, 20) for i in range(6)] for i in range(6)]
print(matrix)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print('{:4d}'.format(matrix[i][j]), end='')
    print()

print(u'\u221e')
