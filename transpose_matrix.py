def matrix_change(matrix):
    return matrix[::-1]

#output target
'''
[[7,4,1],
 [8,5,2],
 [9,6,3]]
'''
def matrix_trans(matrix):
    duplicate_matrix = [[] for i in range(len(matrix))]
    matrix = matrix_change(matrix)
    for row in range(len(matrix)):
        for column in range(len(matrix)):
            duplicate_matrix[column].append(matrix[row][column])
    return duplicate_matrix
         
def display_matrix(matrix):
    for row in matrix:
        for ele in row:
            print(ele,end = " ")
        print()
    
   

def main():
    print("ROTATE IMAGE PROBLEM")
    mt = [[1,2,3],
          [4,5,6],
          [7,8,9]]
    print("Before: ")
    display_matrix(mt)
    trans_mt = matrix_trans(mt)
    print("After: ")
    display_matrix(trans_mt)

    
    


if __name__ == "__main__":
    main()


            
