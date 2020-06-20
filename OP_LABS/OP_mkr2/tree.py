class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.left = None
        self.right = None

    def insertLeft(self, newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.left
            self.left = t

    def insertRight(self, newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.right
            self.right = t
    def getRight(self):
        return self.right
    def getLeft(self):
        return self.left
    def getRoot(self):
        return self.key

    def create_from_string(self, string):
        tree = BinaryTree(string[0])
        for i in range(1, len(string)):
            if ord(string[i]) >= ord(tree.key):
                tree.insertRight(string[i])
            else:
                tree.insertLeft(string[i])

    def find_leaf_max(self):
        while self.right != None:
            self.key = self.right
        return self.key


print("Written in Python 3,\nAssignment completed by Kochev Hennadii, IP-91,\nip9113, variant (13+91)%27+1 = 24\n")

myString = "mynameistor"

