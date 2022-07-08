class Node:
    def __init__(self, data):  # constructor that takes in 3 parameters
        self.left = None  # left subtree
        self.right = None  # right subtree
        self.data = data  # data within node

    # following insert rule is specific to binary trees
    def insert(self, data):
        if self.data == None:
            self.data = data
        else:
            if data < self.data:
                if self.left == None:
                    self.left = Node(data)
                else:
                    # recursion
                    self.left.insert(data)

            elif data > self.data:
                if self.right == None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)


# tree creation
root = Node('g')
root.insert('c')
root.insert('b')
root.insert('a')
root.insert('e')
root.insert('d')
root.insert('f')
root.insert('i')
root.insert('h')
root.insert('j')
root.insert('k')

