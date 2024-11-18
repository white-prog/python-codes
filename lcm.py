def lcm(lis,a,b):
    new_li = []
    for i in lis:
        if i % a == 0 and i % b == 0:
            new_li.append(i)
    return min(new_li)

def main():
    array = [77,66,54,99,78]
    print(lcm(array,6,11))

if __name__ == "__main__":
    # This block runs only if the script is executed directly
    print("This script is being run directly.")
    main()
else:
    # This block can be executed when the module is imported
    print("The script has been imported as a module.")
    #main() = > if we plan to import 