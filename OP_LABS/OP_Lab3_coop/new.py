class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, size):
        self.size = size
        self.elementsIn = 0
        self.slots = [None for i in range(self.size)] 

    def hashFunction(self, key):
        hash = 0
        R = 31
        for i in range(len(key)):
            hash = (R * hash + ord(key[i])) % self.size
        return hash

    def refresh(self):
        self.size *= 2
        self.elementsIn = 0
        self.slots = [None for i in range(self.size)]
    
    def insert(self, key, value):
        self.elementsIn += 1

        index = self.hashFunction(key)
        
        if self.slots[index] == None:
            self.slots[index] = Node(key, value)
            return

        node = self.slots[index]
        prev = node

        while node is not None:
            prev = node
            node = node.next

        prev.next = Node(key, value)


    def find(self, key):
        index = self.hashFunction(key)

        node = self.slots[index]
        while node is not None and node.key != key:
            node = node.next

        if node is None:
            return None
        else:
            return node.value


    def fillUp(self, file):
        with open(file) as f:
            for line in f:
                words = line.split(';')
                key = words[0]
                value = line
                self.insert(key, value)
                if self.elementsIn > 0.8*self.size:
                    self.refresh()
                    print('Refreshing...')
                    self.fillUp(file)

            

#### Testing
file = 'dict_processed.txt'
size = 5
ht = HashTable(size)
ht.fillUp(file)


while input("Type 'exit' to exit: ") != 'exit':
    userword = input('Type word: ').upper()
    result = ht.find(userword)
    if result != None:
        print(result)
    else:
        print('Sorry, my dictionary has no such word...')
        


    
