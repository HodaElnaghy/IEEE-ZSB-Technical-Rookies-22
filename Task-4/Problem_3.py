from turtle import position


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, Node):
        self.head = Node

    # list_length
    def length(self):
        currentNode = self.head
        length = 0
        while currentNode is not None:
            length += 1
            currentNode = currentNode.next
        return length

    # insert at index
    def insertAt(self, data, index):
        newNode = Node(data)

        if index < 0 or index > self.length():  # check validity
            print("Invalid Index")
            return

        if index == 0:  # inserting at index 0
            tempNode = self.head
            self.head = newNode
            self.head.next = tempNode
            return

        currentNode = self.head  # inseting at index
        currentIndex = 0
        while True:
            if currentIndex == index:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentIndex += 1

    # to insert a node at the end of the list
    def insert(self, Node):
        if self.head is None:
            self.head = Node
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = Node

    # print list
    def print_List(self):
        if self.head is None:
            print("List is Empty")
            return
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next

    # Delete at Index:
    def deleteAt(self, index):
        if self.head is None:
            print("Linke List is empty, Delete Failed ")
            return
        if index == 0:
            prevHead = self.head
            self.head = self.head.next
            prevHead.next = None
            return
        currentNode = self.head
        currentIndex = 0
        while True:
            if currentIndex == index:
                prevNode.next = currentNode.next
                currentNode.next = None
                break
            prevNode = currentNode
            currentNode = currentNode.next
            currentIndex += 1

    # Counting the Number of Occurrences of an Element in the Linked List using recursion
    def count_Occurence(self, data):
        return self.count_helper(self.head, data)

    def count_helper(self, current, data):
        if current is None:
            return 0

        if current.data == data:
            return 1 + self.count_helper(current.next, data)
        else:
            return self.count_helper(current.next, data)


if __name__ == '__main__':
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    node4 = Node(40)
    node5 = Node(30)
    linked1 = LinkedList(node1)
    node1.next = node2
    linked1.insertAt(15, 1)
    linked1.insert(node3)
    linked1.insert(node4)
    linked1.insert(node5)
    linked1.insertAt(30, 6)
    linked1.deleteAt(0)
    linked1.deleteAt(3)
    linked1.print_List()
    print(linked1.count_Occurence(30))

