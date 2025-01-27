import time


def stoneinJewel(stone,jewel):
    stone_cnt = 0
    for i in list(jewel):
        if i in list(stone):
            stone_cnt += 1
    return stone_cnt

def main():
    print("STONE IN JEWEL")
    while True:
        stone = input("Enter stone string: ")
        jewel = input("Enter jewel string: ")
        time.sleep(1)
        print("++++++++++++++++++++++++")
        print(stoneinJewel(stone,jewel))
        print("++++++++++++++++++++++++")
        exit_code = input("Enter X to exit nothing to continue: ")
        time.sleep(1)
        if exit_code == "X":
            print("Thank you")
            break

if __name__ == "__main__":
    main()


