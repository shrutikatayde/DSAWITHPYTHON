class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def add(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

    def printList(self, first=None):
        self.first = first
        first = self.head
        if self.head is None:
            print("List is empty")

        while first is not None:
            print(first.data, "->", end=" ")
            first = first.next
        print("None")


obj = LinkedList()
obj.add(8)
obj.printList()
obj.add(4)
obj.printList()
obj.add(6)
obj.printList()

