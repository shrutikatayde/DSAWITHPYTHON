class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if not self.is_empty():
            self.queue.pop(0)
        else:
            raise IndexError("Queue Underflow")

    def get_front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("Queue Underflow")

    def get_rare(self):
        if not self.is_empty():
            return self.queue[-1]
        else:
            raise IndexError("Queue Underflow")

    def size(self):
        return len(self.queue)


if __name__ == "__main__":
    obj_Queue = Queue()
    try:
        print(obj_Queue.get_front())
    except IndexError as e:
        print(e.args[0])

    obj_Queue.enqueue(90)
    obj_Queue.enqueue(30)
    obj_Queue.enqueue(40)
    obj_Queue.enqueue(10)

    print("Front: ", obj_Queue.get_front(), "and Rear: ", obj_Queue.get_rare())
    print("Size: ", obj_Queue.size())
