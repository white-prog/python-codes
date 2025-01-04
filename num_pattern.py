def patternize(n):
    for i in range(1,n+2):
        for j in range(1,i):
            print(j,end = " ")
        print()

def main():
    print("NUMBER PATTERN HALF PYRAMID")
    while True:
        number = int(input("Enter number: "))
        patternize(number)
        choice = input("Type 'X' to exit: ")
        if choice == 'X':
            print("Good bye")
            break

if __name__ == "__main__":
    main()