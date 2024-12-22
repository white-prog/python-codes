import time 


def main():
    counter = int(input("Enter the countdown time in seconds: "))
    while counter > 0:
        print(f"Time left : {counter}")
        time.sleep(1)
        counter -= 1
    print("Time's up")

if __name__ == "__main__":
    main()

