# Chck Even or Odd number
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Find the largest of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest =", a)
elif b > a:
    print("Largest =", b)
else:
    print("Both numbers are equal")