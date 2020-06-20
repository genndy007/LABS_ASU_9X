from math import floor
class Block:
    def __init__(self, size=20):
        self.size = size
        self.content = []

    def binarySearch(self, key):
        arr = self.content

        mid = len(arr) // 2
        low = 0
        high = len(arr) - 1

        while arr[mid][0] != key and low <= high:
            if key > arr[mid][0]:
                low = mid + 1
            else:
                high = mid - 1
            mid = (low + high) // 2

        # if low > high:
        #     print("No such record")
        # else:
        #     print("ID =", mid)
        
        return 'No such record' if low > high else mid

blockSize = 20
records = 200
# Create blocks for 200 records
numBlocks = int(records/blockSize) + 1
main = [Block() for i in range(numBlocks)]

# Adding to certain block
def AddToMain(userinp):
    arr = userinp.split()
    for i in range(len(arr)):
        arr[i] = int(arr[i])

    key = arr[0]
    blockIndex = floor(key/blockSize)
    main[blockIndex].content.append(arr)


## Finding
def SearchInMain(key):
    blockIndex = floor(key/blockSize)

    ourBlock = main[blockIndex]
    subArrIndex = ourBlock.binarySearch(key)
    return main[blockIndex].content[subArrIndex][1]

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


