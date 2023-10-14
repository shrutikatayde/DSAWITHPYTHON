class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def add(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head

    def delFirst(self):
        temp = self.head
        temp = temp.next
        self.head = temp
        self.tail.next = self.head

    def delLast(self):
        secondLast = self.head
        lastNode = secondLast.next

        while lastNode.next is not self.head:
            secondLast = lastNode
            lastNode = lastNode.next
        secondLast.next = self.head
        self.tail = secondLast
        # self.tail.next = self.head

    def delAtSpecificLocation(self, p):
        secondLast = self.head
        lastNode = secondLast.next

        for i in range(0, p - 1):
            secondLast = lastNode
            lastNode = lastNode.next
            if lastNode is None:
                break

        secondLast.next = lastNode.next

    def printList(self):
        if self.head is None:
            print("List is empty")
        else:
            current_node = self.head
            while True:
                print(current_node.data, "->", end=" ")
                current_node = current_node.next
                if current_node is self.head:
                    break
            print("None")


obj = LinkedList()

obj.add(5)
obj.printList()

obj.add(4)
obj.printList()

obj.add(6)
obj.printList()

obj.add(8)
obj.printList()

obj.delFirst()
obj.printList()

obj.delLast()
obj.printList()

obj.delAtSpecificLocation(0)
obj.printList()
