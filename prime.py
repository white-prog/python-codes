def isPrime(num):
    if num < 2:
        return "Not prime"
    for i in range(2,num):
        if num % i == 0:
            return "Not prime"
    return "prime"
print(isPrime(int(input("Enter number: "))))

