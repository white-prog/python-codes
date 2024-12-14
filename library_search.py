def search_target(sorted_lis,target):
    low = 0
    high = len(sorted_lis) - 1
    while low <= high:
        mid = (low + high) // 2
        midValue = sorted_lis[mid][0]
        midIndex = sorted_lis[mid][1]
        if midValue == target:
            return ["Found",midIndex]
        elif target < midValue:
            high = mid - 1
        else:
            low = mid + 1
    return "Not found"

def main():
    import time
    #book_name : shelf id
    book_shelf = {
        "Sapiens history of human kind":125,
        "Brief history of time":130,
        "Cosmos":142,
        "Algorithms and data structure in python":140,
        "Homo naledi":110,
        "C programming":119
        }
    book_sorted = sorted(book_shelf.items())
    admins = {"sabin":"12345s4"}
    print(" LIBRARY ")
    time.sleep(2)
    print("authentication......")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in admins.keys():
        if password == admins[username]:
            print("Check book shelf Id: ")
            book = input("Enter book name: ")
            print(search_target(book_sorted,book))
        else:
            print("Password is not correct process aborted")
    else:
        print("Username not found")
        print("Run this script one more")



if __name__ == "__main__":
    main()