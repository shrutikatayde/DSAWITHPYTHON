class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)


s1 = Stack()
s1.push(1)
s1.push(2)
s1.push(3)
print(s1.items)
print("Top element: ", s1.peek())
print("Removed element: ", s1.pop())
print("Top element: ", s1.peek())
print()

# -------------------------------------------------------------------------------------------------------------------


# stack = []

# <---------INSERTION-------->
# stack.append(8)
# stack.append(7)
# stack.append(4)
# stack.append(5)
# print("after push-->", stack)

# <---------DELETION--------->
# stack.pop(3)
# print("after pop-->", stack)

# <-----------TOP------------>
# top = stack[-1]
# print("peek-->", top)

# <---------TRAVERSAL-------->
# for ele in stack:
#     # stack.pop()
#     # stack.append(8)
#     print(ele, " <- ", end=" ")
# print("top")
