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

    # <<<<<<<<<<<<<<<<----------Searching element in linkedlist------------>>>>>>>>>
    def search(self, x):
        current_node = self.head
        while current_node is not None:
            if current_node.data == x:
                print("element found")
            current_node = current_node.next

    # <<<<<<--------------------printing linkedlist ---------------------->>>>>>>>>>>
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

obj.add(8)
obj.printList()

obj.add(90)
obj.printList()

obj.search(90)
