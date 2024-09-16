def parity(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

def parity_list(lis):
    return [parity(i) for i in lis]

lis = [5,5,7,2,9,0]


import time
time.sleep(3)
print("List of parirty")
print(parity_list(lis))