class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def add(self, data):
        newNode = Node(data)
        current = self.head
        if self.head:
            while current.next is not None:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def iterativeReverse(self):
        if self.head is None:
            return
        prev = self.head
        current = self.head.next

        while current is not None:
            nextNode = current.next
            current.next = prev

            prev = current
            current = nextNode

        self.head.next = None
        self.head = prev

    def recursiveReverse(self, current, prev=None):
        if current is None:
            self.head = prev
            return

        nextNode = current.next
        current.next = prev
        self.recursiveReverse(nextNode, current)

    def printList(self, first=None):
        self.first = first
        first = self.head
        if self.head is None:
            print("List is empty.")
        while first is not None:
            print(first.data, "->", end=" ")
            first = first.next
        print("None")


obj = LinkedList()
obj.add(6)
obj.printList()
obj.add(5)
obj.printList()
obj.add(8)
obj.printList()

obj.iterativeReverse()
obj.printList()

obj.recursiveReverse(obj.head)
obj.printList()
