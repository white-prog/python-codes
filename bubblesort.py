#def swap(num1,num2):
  #  temp = num1
  #  num1 = num2
  #  num2 = temp


arr = [2,1,5,7,3,4,8]
for i in range(len(arr)):
    for j in range(len(arr) - 1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp
print(arr)


