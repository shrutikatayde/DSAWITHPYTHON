class Stack(list):  # here Stack class is subclass of parent class List
    def is_empty(self):
        return len(self) == 0

    def push(self, data):
        self.append(data)

    def pop(self):  # overridden method
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self[-1]

        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self)

    def insert(self, index, data):
        raise AttributeError("No attribute 'insert' in Stack")


s1 = Stack()
# s1.insert(0, 10) # raise error
s1.push(10)
s1.push(20)
s1.push(30)
print("Top value: ", s1.peek())
print("removed value: ", s1.pop())
print("top value: ", s1.peek())
