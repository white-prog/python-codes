import threading
import time
import random
def print_numbers():
    for i in range(4):
        print("A")
        time.sleep(0.1)

def print_letters():
    for i in range(4):
        print("B")
        time.sleep(0.1)


# Creating threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Starting threads
thread1.start()
thread2.start()

# Waiting for threads to complete
thread1.join()
thread2.join()
