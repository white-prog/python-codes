import time

def main():
    counter = 1
    inp = int(input("Enter how much time to run stop watch: "))
    for i in range(inp):
        print(f"[+] {counter}")
        time.sleep(1)
        counter += 1
    

if __name__ == "__main__":
    main()

