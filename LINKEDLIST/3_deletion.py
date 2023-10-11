class Node:
    def __init__(self, data, next=None):
        self.data = data  # actual data
        self.next = next  # address of next node

class LinkedList:
    def __init__(self, head=None):
        self.head = head  # start node

    def add(self, data):
        new_node = Node(data)

        if self.head:  # if head is present
            current_node = self.head
            while current_node.next is not None:  # if head/next node is not null
                current_node = current_node.next  # go to the end of the linked list

            current_node.next = (
                new_node  # after reaching at end last node refers to the new node
            )
        else:  # if head is null
            self.head = new_node  # set head to new node

    # ------------------------------------------------------------------------------------------------------------------

    def delFirst(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next

    def delLast(self):
        current_node = self.head
        if current_node is None:
            print("List is empty")
            return

        if current_node.next is None:
            self.head = None
            return

        secondLast = current_node
        lastNode = current_node.next

        while lastNode.next is not None:
            lastNode = lastNode.next
            secondLast = secondLast.next

        secondLast.next = None

    # <<<<<<<<<<<-------------PRINTING LINKED LIST------------------>>>>>>>>>>>>

    def printList(self, first=None):  # for printing linked list
        if self.head is None:
            print("list is empty")
            return
        self.first = first
        first = (
            self.head
        )  # assign head to first for starting liked list as head is start
        while first:
            print(first.data, " --> ", end=" ")  # print the data at first node
            first = first.next  # goto to next node
        print("None")


obj = LinkedList()

obj.add(5)
obj.printList()

obj.add(3)
obj.printList()

obj.add(2)
obj.printList()


obj.delFirst()
obj.printList()

obj.delLast()
obj.printList()
