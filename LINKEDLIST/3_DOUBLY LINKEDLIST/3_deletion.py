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
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode

    def delFirst(self):
        temp = self.head
        temp = temp.next
        self.head = temp
        self.head.prev = None

    def delLast(self):
        temp = self.tail
        temp = temp.prev
        temp.next = None

    def delMid(self, p):
        prevNode = self.head
        currentNode = prevNode.next
        for i in range(1, p - 1):
            prevNode = currentNode
            currentNode = currentNode.next
        prevNode.next = currentNode.next
        currentNode.next.prev = prevNode

    def printList(self, first=None):
        self.first = first
        first = self.head
        if first is None:
            print("list is empty")
        while first:
            print(first.data, "->", end=" ")
            first = first.next
        print("None")


obj = LinkedList()
obj.add(8)
obj.add(9)
obj.add(5)
obj.add(4)
obj.add(4)
obj.printList()
obj.delFirst()
obj.printList()
obj.delLast()
obj.printList()
obj.delMid(2)
obj.printList()
