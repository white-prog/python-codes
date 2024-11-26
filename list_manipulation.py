def manipulate(lis):
    l = []
    for i in lis:
        if i % 2 == 0:
            l.append(i ** 2)
        else:
            l.append(i ** 3)
    return l




def main():
    li = [1,2,3,4,5,6]
    print(manipulate(li))

if __name__ == "__main__":
    main()