movies = ["Inception","Titanic","The matrix","Schindler's List"]
def titleLength(lis,max_length):
    new_lis = []
    for i in lis:
        if len(i) < max_length:
            new_lis.append(i)
    return new_lis

print(titleLength(movies,10))

