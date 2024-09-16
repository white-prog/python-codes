def to_usd(r):
    return r*0.012

i = 0
while i <= 5:
    ind = float(input("enter indian rs: "))
    print(to_usd(ind))
    i+=1


