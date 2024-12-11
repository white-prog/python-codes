#functions are mini program inside program , it is a black box takes input and return outputs 
def hello(name):
    print(" ".join(["Hello",name]))

def checksNumber(number):
    isPrime = False
    if number >= 2:
        isPrime = True
        for i in range(2,number):
            if number % i == 0:
                isPrime = False
                break
    return isPrime


global num1 
num1 = 90





def main():
    import random
    hello("Random")
    value_list = []
    value_list = [random.randint(1,100) if random.randint(1,50) not in value_list else random.randint(50,100) for i in range(10)]
    prime_list = [checksNumber(i) for i in value_list]
    for i in zip(value_list,prime_list):
        if i[1] == True:
            val = "Prime"
        else:
            val = "Not Prime"
        print(f"{i[0]} : {val}")
    
    print(num1)


if __name__ == "__main__":
    main()
    
    
