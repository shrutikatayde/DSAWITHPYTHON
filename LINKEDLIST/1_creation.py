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

obj.add(7)
obj.printList()
obj.add(4)
obj.printList()
obj.add(7)
obj.printList()
