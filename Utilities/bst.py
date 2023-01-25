'''
Basic Binary Tree Code
Reference: https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm
'''
class Node:
    def __init__(self, data): #Node constructor
        self.left = None
        self.right = None
        self.data = data
    def printSelf(self): #Print value of the node
        print(self.data)
    def insert(self, data): #Insert new data
        if self.data: #Node currently has data thus place it on child nodes
            if data < self.data: #Data being inserted is less than current node
                if self.left is None: #Empty left child node
                    self.left = Node(data)
                else: #Left contains something, create its child node
                    self.left.insert(data)
            elif data > self.data: #Data being inserted is more than current node
                if self.right is None: #Empty right child node
                    self.right = Node(data)
                else: #Right contains something, create its child node
                    self.right.insert(data)
        else:
            self.data = data
    def printTree(self): #Process goes by printing the left then middle then right nodes of the tree.
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()
    def inOrderTraversal(self, root): #Left Root Right
        res = []
        if root:
            res = self.inOrderTraversal(root.left)
            res.append(root.data)
            res = res + self.inOrderTraversal(root.right)
        return res
    def preOrderTraversal(self, root): #Root Left Right
        res = []
        if root:
            res.append(root.data)
            res = res + self.preOrderTraversal(root.left)
            res = res + self.preOrderTraversal(root.right)
        return res
    def postOrderTraversal(self, root): #Left Right Root
        res = []
        if root:
            res = self.postOrderTraversal(root.left)
            res = res + self.postOrderTraversal(root.right)
            res.append(root.data)
        return res
    def treeAsList(self): #Returns tree into list; Similar to inOrderTraversal but self made
        ls = []
        if self.left:
            ls = ls + self.left.treeAsList()
        ls.append(self.data)
        if self.right:
            ls = ls + self.right.treeAsList()
        return ls
    def getChildren(self, root):
        if not root:
            return None
        left = None
        right = None
        if root.left:
            left = root.left.data
        if root.right:
            right = root.right.data
        return [left,right]

#Create Tree
entries = [6,4,2,1,3,5,7]
initial = True
root = None
for e in entries:
    if initial:
        initial = False
        root = Node(e)
    else:
        root.insert(e)

#Print Tree
print("Tree: ")
root.printTree()

print("\nTree as List: ")
print(root.treeAsList())

print("\nTraversal: ")
print(root.preOrderTraversal(root))
print(root.inOrderTraversal(root))
print(root.postOrderTraversal(root))

print("\nChildren")
print("Children of " + str(root.data), root.getChildren(root))
print("Children of " + str(root.right.data), root.getChildren(root.right))