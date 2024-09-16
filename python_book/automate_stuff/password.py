passwordFile = open("secretpass.txt")
password = passwordFile.read()
typepassword = input("Enter password: ")

if typepassword == password:
    print("Access granted")
else:
    print("Access denied")