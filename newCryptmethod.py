def encrypt_val(val):
    import random
    k1 = random.randint(0,len(val))
    k2 = random.randint(0,len(val))
    if k1 == k2:
        k2 = k1 + 1
    vl = list(val)
    temp = vl[k1]
    vl[k1] = vl[k2]
    vl[k2] = temp
    return ("#".join(vl),k1,k2)
def decrypt_val(valu,ky1,ky2):
    valu_str = valu.split("#")
    temp = valu_str[ky1]
    valu_str[ky1] = valu_str[ky2]
    valu_str[ky2] = temp
    return "".join(valu_str)


def main():
    print("CRYPTO TRY")
    
    user_input = input("Encryption -> E or Decryption -> D: ")
    value = input("Enter value: ")
    if user_input == 'E':
        print(encrypt_val(value))
    else:
        key1 = int(input("Enter first value: "))
        key2 = int(input("Enter second value: "))
        print(decrypt_val(value,key1,key2))

if __name__ == "__main__":
    main()

