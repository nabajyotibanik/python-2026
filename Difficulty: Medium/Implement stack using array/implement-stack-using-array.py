class myStack:
    def __init__(self, n):
        self.arr = []
        self.n = n

    # Push element x into stack
    def push(self, x):
        if len(self.arr) < self.n:
            self.arr.append(x)

    # Remove top element
    def pop(self):
        if len(self.arr) == 0:
            return -1
        return self.arr.pop()

    # Return top element
    def peek(self):
        if len(self.arr) == 0:
            return -1
        return self.arr[-1]

    # Check if stack is empty
    def isEmpty(self):
        return len(self.arr) == 0

    # Check if stack is full
    def isFull(self):
        return len(self.arr) == self.n