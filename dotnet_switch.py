def dotnet():
    import time
    print("Dotnet switch")
    time.sleep(4)
    print("........")

def main():
    dotnet()
    print((2 == 0) == False)

if __name__ == "__main__":
    main()