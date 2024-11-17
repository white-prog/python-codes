class Stack:
    def __init__(self):
        self.arr = []
        self.size = -1
    def push(self,value):
        self.arr.append(value)
        self.size += 1
    def pop(self):
        if  self.size < 0:
            return "index error"
        self.arr.remove(self.arr[self.size])
    def display(self):
        print(self.arr)

stack = Stack()
stack.push(5)
stack.push(4)
stack.push(6)
stack.pop()
stack.display()

