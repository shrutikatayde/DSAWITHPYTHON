class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def add(self, data):
        newNode = Node(data)
        current = self.head
        if self.head:
            while current.next is not self.head:
                current = current.next
            current.next = newNode
            tail = newNode
            tail.next = newNode
            newNode.next = self.head

        else:
            self.head = newNode
            tail = newNode
            tail.next = self.head

    def printList(self, first=None):
        self.first = first
        first = self.head
        if first is None:
            print("List is empty.")

        current = first
        # print(current.data)

        while True:
            print(current.data, "-->", end=" ")
            current = current.next
            if current is self.head:
                break
        print("None")


obj = LinkedList()

obj.add(8)
obj.printList()
obj.add(5)
obj.printList()
obj.add(6)
obj.printList()
obj.add(2)
obj.printList()
