class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def addFirst(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def addLast(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode

    def addMid(self, data, p):
        self.p = p
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            prevNode = self.head
            currentNode = prevNode.next

            for i in range(1, p - 1):
                prevNode = currentNode
                currentNode = currentNode.next
            newNode.prev = prevNode
            newNode.next = prevNode.next
            prevNode.next = newNode
            currentNode.prev = newNode

    def printList(self, first=None):
        self.first = first
        first = self.head
        if self.head is None:
            print("list is empty")
        while first:
            print(first.data, "->", end=" ")
            first = first.next
        print("None")


obj = LinkedList()
obj.addFirst(8)
obj.printList()
obj.addFirst(7)
obj.printList()
obj.addFirst(6)
obj.printList()


obj.addLast(8)
obj.printList()
obj.addLast(7)
obj.printList()
obj.addLast(6)
obj.printList()

obj.addMid(65, 3)
obj.printList()
