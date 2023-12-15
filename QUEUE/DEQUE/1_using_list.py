class Deque:
    def __init__(self):
        self.ele = []

    def is_empty(self):
        return len(self.ele) == 0

    def insert_front(self, data):
        self.ele.insert(0, data)

    def insert_rear(self, data):
        self.ele.append(data)

    def delete_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            self.ele.pop(0)

    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Deueue is empty")
        else:
            self.ele.pop()

    def get_front(self):
        if self.is_empty():
            raise IndexError("Deueue is empty")
        else:
            return self.ele[-1]

    def get_rear(self):
        if self.is_empty():
            raise IndexError("")

    def get_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty.")
        else:
            return self.ele[0]

    def get_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty.")
        else:
            return self.ele[-1]

    def size(self):
        return len(self.ele)

d1 = Deque()
d1.insert_front(20)
d1.insert_front(90)
d1.insert_rear(10)
d1.insert_rear(40)
print("front", d1.get_front(), "rear", d1.get_rear())
