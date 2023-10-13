class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def add(self, data):
        new_node = Node(data)
        if self.head:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = new_node
        else:
            self.head = new_node

    def sorting(self):
        current_node = self.head
        lst = []
        while current_node:
            lst.append(current_node.data)
            current_node = current_node.next
        lst.sort()
        new = LinkedList()
        for i in lst:
            new.add(i)
        new.printList()

    def printList(self, first=None):
        current_node = self.head
        if current_node is None:
            print("List is empty")

        self.first = first
        first = self.head
        while first:
            print(first.data, "->", end=" ")
            first = first.next
        print(None)


obj = LinkedList()

obj.add(9)
obj.printList()
obj.add(6)
obj.printList()
obj.add(8)
obj.printList()
obj.sorting()
