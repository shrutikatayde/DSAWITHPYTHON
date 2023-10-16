class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def addFirst(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head

    def addLast(self, data):
        new_node = Node(data)
        if self.head:
            # current_node = self.head
            # while current_node.next is not self.head:
            #     current_node = current_node.next
            # current_node.next = new_node

            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head

    def addMid(self, data, x):
        self.x = x
        new_node = Node(data)
        current = self.head
        while current.next is not self.head:
            if current.data == x:
                new_node.next = current.next
                current.next = new_node
            current = current.next

    def addAtSpecificLocation(self, data, p):
        new_node = Node(data)
        current = self.head
        for i in range(0, p - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def printList(self, first=None):
        self.first = first
        first = self.head
        if self.head is None:
            print("list is empty")
        while True:
            print(first.data, "->", end=" ")
            if first.next is self.head:
                break

            first = first.next

        print("None")


obj = LinkedList()

obj.addFirst(8)
obj.printList()
obj.addFirst(5)
obj.printList()
obj.addFirst(6)
obj.printList()
obj.addFirst(2)
obj.printList()

print()

obj1 = LinkedList()
obj1.addLast(8)
obj1.printList()
obj1.addLast(5)
obj1.printList()
obj1.addLast(6)
obj1.printList()
obj1.addLast(2)
obj1.printList()

print()

obj1.addMid(99, 6)
obj1.printList()

print()

obj1.addAtSpecificLocation(38, 2)
obj1.printList()
