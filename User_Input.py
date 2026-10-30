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


# Calculate the area of a rectangle
length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width

print("Area =", area)

# Age Calculator
name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))

age = 2026 - birth_year

print("Hello", name)
print("Your age is:", age)

# Shopping Bill 
item = input("Enter item name: ")
price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print("Item:", item)
print("Quantity:", quantity)
print("Total Bill:", total)