def swap(num1,num2):
  temp = num1
  num1 = num2
  num2 = temp
  return [num1,num2]


arr = [2,1,5,7,3,4,8]
for i in range(len(arr)):
    for j in range(len(arr) - 1):
        if arr[j] > arr[j+1]:
            value = swap(arr[j],arr[j + 1])
            arr[j] = value[0]
            arr[j + 1] = value[1]
print(arr)


