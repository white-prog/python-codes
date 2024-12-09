def binary_search(sortedArray,target):
    low = 0
    high = len(sortedArray) - 1
    while low <= high :
        mid = (low + high) // 2
        if sortedArray[mid] == target:
            return [mid,True,target]
        elif sortedArray[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return ["not found",False,target]

def main():
    array = [1,2,3,4,5,6,7,8]
    print("INDEX : FOUND OR NOT : TARGET")
    print(binary_search(array,1))
    print(binary_search(array,2))
    print(binary_search(array,3))
    print(binary_search(array,4))
    print(binary_search(array,5))
    print(binary_search(array,6))
    print(binary_search(array,7))
    print(binary_search(array,8))
    print(binary_search(array,9))

if __name__ == "__main__":
    main()
    



