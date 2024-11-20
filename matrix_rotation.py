

def rotate_matrix(value):
    li = []
    for row in range(len(value)):
        val = [i[row] for i in value][::-1]
        li.append(val)
    return li

def main():
    matrix = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
    print(rotate_matrix(matrix))
    

if __name__ == "__main__":
    print("Rotated matrix : ", end = "")
    main()




