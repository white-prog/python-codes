class Queue:
    def __init__(self):
        self.array = []
        self.size = len(self.array)
    def enque(self,val):
        self.array.insert(0,val)
    def deque(self):
        self.array.remove(self.array[self.size - 1])
    def displayQueue(self):
        print(" -> ".join([str(i) for i in self.array]))

if __name__ == "__main__":
    print("Exported to another file")

    

    