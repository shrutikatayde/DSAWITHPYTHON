import array as array


class Stack:
    def __init__(self):
        self.top = -1
        self.n = int(input("Enter the size of the stack: "))
        self.arr = array.array("i", [])

    def push(self):
        if self.top == (self.n - 1):
            print("Overflow")
        else:
            i = int(input("Enter element: "))
            self.top = self.top + 1
            self.arr.insert(
                self.top, i
            )  # Use the append method to add elements to the array
            print("Item inserted")

    def pop(self):
        if self.top == -1:
            print("Underflow")
        else:
            self.top = self.top - 1
            print("Item deleted")

    def display(self):
        print("Items are:")
        for i in range(self.top, -1, -1):  # Corrected the range to include 0
            print(self.arr[i])


if __name__ == "__main__":
    obj = Stack()
    obj.push()
    obj.push()
    obj.push()
    obj.push()
    obj.display()
