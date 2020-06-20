import random

class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.elementsIn = 0
        self.slots = [None for i in range(self.size)] 

    def MurmurHash2A(self, key, seed=13):
        m = 0x5bd1e995
        r = 24
        l = self.size

        data = key

        h = seed

        while l >= 4:
            for char in data:
                k = ord(char)

            # mmix(h,k)
            k *= m
            k ^= k >> r
            k *= m 
            h *= m 
            h ^= k

            l -= 4

            h %= self.size
        

        t = 0
        if l == 3:
            t ^= data[2] << 16
        elif l == 2:
            t ^= data[1] << 8
        elif l == 1:
            t ^= data[0]

        # mmix(h,t)
        t *= m
        t ^= t >> r
        t *= m 
        h *= m 
        h ^= t
        h %= self.size
        # mmix(h,l)
        l *= m
        l ^= l >> r
        l *= m 
        h *= m 
        h ^= l


        return h % self.size

    def insert(self, key, value):
        self.elementsIn += 1

        k = 1
        i = 0
        index = self.MurmurHash2A(key)

        while self.slots[index] != None:
            i += 1
            index = (index + i*k) % self.size

        self.slots[index] = Pair(key, value)

    def find(self, key):
        compare_index = 1
        index = self.MurmurHash2A(key)
        k = 1
        i = 0

        while (self.slots[index] is None or self.slots[index].key != key) and i <= self.size:
            index = (index + i*k) % self.size
            i += 1
            compare_index += 2
        
        print("Comparisons of index value:", compare_index)

        if self.slots[index] is None or self.slots[index].key != key:
            return None
        else:
            return self.slots[index].value

    def refresh(self):
        self.size *= 2
        self.elementsIn = 0
        self.slots = [None for i in range(self.size)]

    def fillUp(self, numElements):
        keyLength = 20
        valueLength = 200
        oneKey = True
        needToRefresh = False
        for times in range(numElements):
            key = PseudoRandomStringsGenerator(keyLength)
            if oneKey:
                oneKey = False
                print(key)
            value = PseudoRandomStringsGenerator(valueLength)
            self.insert(key, value)
            if self.elementsIn > 0.8*self.size:
                needToRefresh = True
                break

        if needToRefresh:
            self.refresh()
            print('Refreshing...')
            self.fillUp(numElements)

def PseudoRandomStringsGenerator(length):
    string = ""
    for times in range(length):
        string += chr(random.randint(33, 126))
    return string





ht100 = HashTable()
ht100.fillUp(100)
key = input("Type your key for size100: ")
print("Here is value for size100: ", ht100.find(key))

ht1000 = HashTable()
ht1000.fillUp(1000)
key = input("Type your key for size1000: ")
print("Here is value for size1000: ", ht1000.find(key))

ht5000 = HashTable(5000)
ht5000.fillUp(5000)
key = input("Type your key for size5000: ")
print("Here is value for size5000: ", ht5000.find(key))

ht10000 = HashTable(10000)
ht10000.fillUp(10000)
key = input("Type your key for size10000: ")
print("Here is value for size10000: ", ht10000.find(key))

ht20000 = HashTable(20000)
ht20000.fillUp(20000)
key = input("Type your key for size20000: ")
print("Here is value for size20000: ", ht20000.find(key))
