
def pyramid(n):

	for i in range(n):
		for j in range((n * 2) - 1):
			if (i == 0 and j == 2) or (i == 1 and (j == 1 or j == 2 or  j == 3 )) or (i == 2 and j >= 0):
				print("x",end="")
			else:
				print(" ",end="")
		print()

pyramid(3)

#work for pyramid of 3 values not more logic is incorrect and do another **