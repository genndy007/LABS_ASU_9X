### Functions and classes
from math import floor
from random import randint

class Block:
    def __init__(self, size=100):
        self.size = size
        self.content = []

    def binarySearch(self, key):
        arr = self.content

        mid = len(arr) // 2
        low = 0
        high = len(arr) - 1
        timesComparing = 0

        while arr[mid][0] != key and low <= high:
            if key > arr[mid][0]:
                low = mid + 1
            else:
                high = mid - 1
            timesComparing += 1
            mid = (low + high) // 2

        print(f"Compared {timesComparing} times")

        return 'No such record' if low > high else mid


# Adding to certain block
def AddToMain(key, value):
    
    blockIndex = floor(key/blockSize)
    main[blockIndex].content.append([key, value])
    main[blockIndex].content.sort()
    # print('Block:', main[blockIndex].content)

## Finding
def SearchInMain(key):
    blockIndex = floor(key/blockSize)

    ourBlock = main[blockIndex]
    subArrIndex = ourBlock.binarySearch(key)
    return 'No such key' if subArrIndex == 'No such record' else main[blockIndex].content[subArrIndex][1]

# Changing
def ChangeValueForKey(key, newValue):
    blockIndex = floor(key/blockSize)

    ourBlock = main[blockIndex]
    subArrIndex = ourBlock.binarySearch(key)
    main[blockIndex].content[subArrIndex][1] = newValue

# Deleting
def DeleteRecordByKey(key):
    blockIndex = floor(key/blockSize)
    ourBlock = main[blockIndex]
    subArrIndex = ourBlock.binarySearch(key)
    main[blockIndex].content.pop(subArrIndex)

def PseudoRandomString():
    text = ''
    for i in range(5):
        num = randint(40, 120)
        char = chr(num)
        text += char
    return text


# Testing
blockSize = 100
records = 10000
numBlocks = int(records/blockSize) + 1
main = [Block() for i in range(numBlocks)]

print("Choose:")
print("Create database with random values: 0")
print("Load database from files: 1")
stateOfStart = int(input())
if stateOfStart == 0:
    print("Your possibilities:")
    print("ADD <key> <value>")
    print("FIND <key>")
    print("EDIT <key> <newValue>")
    print("DELETE <key>")
    print("EXIT")
    # Pushing random key-value pairs to main
    usedNumbers = []
    while len(usedNumbers) < 2000:
        key = randint(0, records-1)
        while key in usedNumbers:
            key = randint(0, records-1)

        usedNumbers.append(key)
        value = PseudoRandomString()
        blockIndex = floor(key/blockSize)
        main[blockIndex].content.append([key, value])
    
    startVal = 0
    indexFile = open("index.txt", "w")
    for block in main:
        
        startVal += 100
        block.content.sort()
        if len(block.content) == 0:
            indexFile.write(f"{startVal} []\n")
        else:
            indexFile.write(f"{startVal} {block.content[0][0]}\n")
    
    indexFile.close()

    while True:
        userinp = input(">>> ")
        command = userinp.split()
        word = command[0]

        if word == 'ADD':
            key = int(command[1])
            value = command[2]
            if key in usedNumbers:
                print("Duplicate is in Main File")
                continue
            AddToMain(key, value)
        elif word == "FIND":
            key = int(command[1])
            value = SearchInMain(key)
            print("Found value:", value)
        elif word == "EDIT":
            key = int(command[1])
            newValue = command[2]
            ChangeValueForKey(key, newValue)
        elif word == "DELETE":
            key = int(command[1])
            DeleteRecordByKey(key)
        elif word == "EXIT":
            mainfile = open('mainfile.txt', 'w')

            for block in main:
                for record in block.content:
                    key = record[0]
                    value = record[1]
                    mainfile.write(f"{key} {value}\n")

            mainfile.close()
            break


elif stateOfStart == 1:
    mainfile = open('mainfile.txt')

    usedNumbers = []
    for line in mainfile:
        key, value = line.split()
        key = int(key)
        usedNumbers.append(key)
        AddToMain(key, value)

    while True:
        userinp = input(">>> ")
        command = userinp.split()
        word = command[0]

        if word == 'ADD':
            key = int(command[1])
            value = command[2]
            if key in usedNumbers:
                print("Duplicate is in Main File")
                continue
            AddToMain(key, value)
        elif word == "FIND":
            key = int(command[1])
            value = SearchInMain(key)
            print("Found value:", value)
        elif word == "EDIT":
            key = int(command[1])
            newValue = command[2]
            ChangeValueForKey(key, newValue)
        elif word == "DELETE":
            key = int(command[1])
            DeleteRecordByKey(key)
        elif word == "EXIT":
            mainfile = open('mainfile.txt', 'w')

            for block in main:
                for record in block.content:
                    key = record[0]
                    value = record[1]
                    mainfile.write(f"{key} {value}\n")

            mainfile.close()
            break