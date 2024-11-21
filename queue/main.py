from queue import Queue

def main():
    theater_queue = Queue()
    theater_queue.enque(2)
    theater_queue.enque(5)
    theater_queue.enque(23)
    theater_queue.enque(7)
    theater_queue.deque()
    theater_queue.displayQueue()

if __name__ == "__main__":
    main()