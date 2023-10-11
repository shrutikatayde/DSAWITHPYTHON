class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    # <<<<-----------ADDING AT THE "BEGINNING" OF THE LINKEDLIST---------->>>>>>>>>>

    def addFirst(self, data):
        new_node = Node(data)
        # if self.head is None:
        #     self.head = new_node
        #     return
        new_node.next = self.head
        self.head = new_node

    # <<<<-----------ADDING AT THE "END" OF THE LINKEDLIST----------------->>>>>>>>>>

    def addLast(self, data):
        new_node = Node(data)

        if self.head:  # if head is present
            current_node = self.head
            while current_node.next is not None:  # if head/next node is not null
                current_node = current_node.next  # go to the end of the linked list

            current_node.next = (
                new_node  # after reaching at end last node refers to the new node
            )

    # <<<<-----------ADDING AT THE "MID" OF THE LINKEDLIST---------->>>>>>>>>>

    def addMid(
        self, data, x
    ):  # x----> given node for adding element to linkedlist after this node
        self.x = x
        new_node = Node(data)
        current_node = self.head
        while current_node:
            if current_node.data == x:
                new_node.next = current_node.next
                current_node.next = new_node
            current_node = current_node.next

    def printList(self, first=None):
        if self.head is None:
            print("The list is empty.")
            return

        self.first = first
        first = self.head
        while first:
            print(first.data, "-->", end=" ")
            first = first.next
        print("None")


obj = LinkedList()

obj.addFirst(8)
obj.printList()

obj.addLast(90)
obj.printList()

obj.addMid(6, 8)
obj.printList()
