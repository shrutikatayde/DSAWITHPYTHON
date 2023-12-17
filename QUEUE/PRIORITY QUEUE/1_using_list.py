class PriorityQueue:
    def __init__(self):
        self.pqueue = []

    def is_empty(self):
        return len(self.pqueue) == 0

    def push(self, data, priority):
        index = 0
        while index < len(self.pqueue) and self.pqueue[index][1] <= priority:
            index += 1
        self.pqueue.insert(index, (data, priority))

    def pop(self):
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        return self.pqueue.pop(0)[0]

    def size(self):
        return len(self.pqueue)


pq = PriorityQueue()
pq.push(10, 3)
pq.push(30, 2)
pq.push(40, 4)
pq.push(21, 1)
print("size: ", pq.size())
print(pq.pqueue)

for i in range(len(pq.pqueue)):
    print(pq.pqueue[i])
print(pq.pop())
print("size: ", pq.size())
