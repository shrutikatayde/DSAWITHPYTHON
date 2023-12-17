class Node:
    def __init__(self, item=None, priority=None, next=None):
        self.item = item
        self.priority = priority
        self.next = next


class PriorityQueue:
    def __init__(self):
        self.start = None
        self.item_count = 0

    def push(self, data, priority):
        newNode = Node(data, priority)
        if self.start is None or priority < self.start.priority:
            newNode.next = self.start
            self.start = newNode
        else:
            temp = self.start
            while temp.next and temp.next.priority <= priority:
                temp = temp.next
            newNode.next = temp.next
            temp.next = newNode
        self.item_count += 1

    def is_empty(self):
        return self.start is None

    def pop(self):
        if self.is_empty():
            raise IndexError("Priority queue is empty.")
        data = self.start.item
        self.start = self.start.next
        self.item_count -= 1
        return data

    def size(self):
        return self.item_count


pq = PriorityQueue()
pq.push(20, 4)
pq.push(30, 2)
pq.push(60, 5)
pq.push(10, 6)

while not pq.is_empty():
    print(pq.pop())
