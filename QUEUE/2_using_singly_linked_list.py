# insertion at rear
# deletion at front
# when queue is empty then we have to make changes in both front and rear
# else we have to make changes in only rear.


class Node:
    def __init__(self, ele=None, next=None):
        self.ele = ele
        self.next = next


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.ele_count = 0

    def is_empty(self):
        return self.front is None  # or self.rear is None or self.ele_count = 0

    def enqueue(self, data):
        newNode = Node(data)
        if self.is_empty():
            self.front = newNode
        else:
            self.rear.next = newNode
        self.rear = newNode
        self.ele_count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Empty Queue")
        elif self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        self.ele_count -= 1

    def get_front(self):
        if self.is_empty():
            raise IndexError("No data in the queue")
        else:
            return self.front.ele

    def get_rear(self):
        if self.is_empty():
            raise IndexError("No data in the Queue")
        else:
            return self.rear.ele

    def size(self):
        return self.ele_count


q = Queue()
q.enqueue(43)
q.enqueue(23)
q.enqueue(25)
q.enqueue(12)

print("front: ", q.get_front(), "rear: ", q.get_rear())

q.dequeue()
print("front: ", q.get_front(), "rear: ", q.get_rear())
