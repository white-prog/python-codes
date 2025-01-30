#number pyramid
def num_pyr(num):
    numbers = 1
    for i in range(1,num+1):
        spaces = " " * (num - i)
        printer = f"{numbers}" * (2 * i- 1)
        print(spaces + printer)
        numbers += 2

def main():
    print("ODD NUMBER PYRAMID")
    num_pyr(5)

if __name__ == "__main__":
    main()


