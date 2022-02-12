class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        else:
            current = self.root
            while True:
                if data == current.data:
                    return
                if data < current.data:
                    if current.left is None:
                        current.left = Node(data)
                        break
                    else:
                        current = current.left
                else:

                    if current.right is None:
                        current.right = Node(data)
                        break
                    else:
                        current = current.right
            current = self.root


def preOrder(root):
    if root is not None:
        print(root.data)
        preOrder(root.left)
        preOrder(root.right)


if __name__ == '__main__':
    tree = BST()
    arr = list(map(int, input().split()))

    for i in arr:
        tree.insert(i)

    print(tree.root.data)
    preOrder(tree.root)
