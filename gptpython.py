#Getting started python
print("Hello World!")

#Variables and data types

name = "Sabin"
print(name)

age = 21
print(age)

height = 5.6
print(height)

is_student = True
print(is_student)

#Basic operator
a = 10
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)

#control structures
num = float(input("Enter number: "))
if num < 0:
    print("negative number")
elif num > 0:
    print("positive number")
else:
    print("zero")

#loop
for i in range(1,11):
    print(i)

i = 1
while i <= 10:
    print(i)
    i += 1
#Function
def add_number(a,b):
    return a + b
num1 = 1
num2 = 4
print(add_number(num1,num2))

#Lists
fruits = ["apple","orange","grapes","dates"]
for fruit in fruits:
    print(fruit)


#tuple
days = ("monday","tuesday","wednesday","friday","saturday")
for day in days:
    print(day)

#dictionary
students = {"sabin":88,"sanjay":91}
for name,grade in students.items():
    print(f"{name}:{grade}")
