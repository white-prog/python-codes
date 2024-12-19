import time


def square(lis):
    for ele in lis:
        for elements in ele:
            print(elements,end = "   ")
        print()







def main():
    game_rules = ["Don't repeat numbers in one row"]
    
    sudoku_template_basic = [['▢' for i in range(3)] for j in range(3)]
    sudoku_copy = sudoku_template_basic
    print("---------------------")
    print("SUDOKU BASIC TEMPLATE")
    print("---------------------")
    square(sudoku_template_basic)
    time.sleep(3)
    print("start game...")
    for i in range(3):
        for j in range(3):
            num = int(input("Enter number : "))
            if num > 9 or num < 1:
                print("Error")
            if num not in sudoku_copy[i]:
                sudoku_copy[i][j] = num
            else:
                sudoku_copy[i][j] = 0
    square(sudoku_copy)
    zeros = 16 - sum([i.count(0) for i in sudoku_copy])
    print(f"score : {zeros * 10}")
        





if __name__ == "__main__":
    main()