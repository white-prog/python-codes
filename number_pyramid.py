import sys

#number pyramid
def num_pyr(num):
    numbers = 1
    for i in range(1,num+1):
        spaces = " " * (num - i)
        printer = f"{numbers}" * (2 * i- 1)
        print(spaces + printer)
        numbers += 2

def main():
    # Check if command line argument is provided
    if len(sys.argv) != 2:
        print("Usage: python number_pyramid.py <height>")
        print("Example: python number_pyramid.py 5")
        return
    
    try:
        height = int(sys.argv[1])
        print(f"ODD NUMBER PYRAMID (Height: {height})")
        num_pyr(height)
    except ValueError:
        print("Error: Please provide a valid integer for height")

if __name__ == "__main__":
    main()


