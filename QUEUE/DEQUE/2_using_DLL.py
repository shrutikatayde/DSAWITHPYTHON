class Node:
    def __init__(self, ele=None, prev=None, next=None):
        self.prev = prev
        self.ele = ele
        self.next = next


class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.ele_count = 0

    def is_empty(self):
        return self.ele_count == 0

    def insert_front(self, data):
        newNode = Node(data, None, self.front)
        if self.is_empty():
            self.rear = newNode
        else:
            self.front.prev = newNode
        self.front = newNode
        self.ele_count += 1

    def insert_rear(self, data):
        newNode = Node(data, self.rear, self.rear.next)
        if self.is_empty():
            self.front = newNode
        else:
            self.rear.next = newNode
        self.rear = newNode
        self.ele_count += 1

    def delete_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty.")
        elif self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self.ele_count -= 1

    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty.")
        elif self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        self.ele_count -= 1

    def get_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty.")
        return self.front.ele

    def get_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty.")
        return self.rear.ele

    def size(self):
        return self.ele_count


deq = Deque()
deq.insert_front(78)
deq.insert_front(3)
deq.insert_rear(8)
deq.insert_rear(7)

print("size: ", deq.size())
print("front: ", deq.get_front())
print("rear: ", deq.get_rear())
deq.delete_front()
deq.delete_rear()
print(deq.size())
