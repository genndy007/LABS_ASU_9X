from block import Block
from math import floor
main = [Block() for i in range(20)]
blockSize = 20

# def PutIntoMainFromText(key, value):
#     blockIndex = floor(key/blockSize)
#     main[blockIndex].content.append([key, value])

with open('database.txt') as db:
    for line in db:
        key, value = line.split()
        key = int(key)
        value = int(value)
        blockIndex = floor(key/blockSize)
        main[blockIndex].content.append([key, value])

for block in main:
    print(block.content)
