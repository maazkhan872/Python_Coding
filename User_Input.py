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

# temperature convert celsius to fahrenheit
print("Temperature Converter")

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit:", fahrenheit)

# Calculate Grade
print("Student Grade Calculator")

name = input("Enter your name: ")
marks = float(input("Enter your marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid Marks!")

elif marks >= 90:
    grade = "A+"
    print(name, "Your Grade is:", grade)

elif marks >= 80:
    grade = "A"
    print(name, "Your Grade is:", grade)

elif marks >= 70:
    grade = "B"
    print(name, "Your Grade is:", grade)

elif marks >= 60:
    grade = "C"
    print(name, "Your Grade is:", grade)

elif marks >= 50:
    grade = "D"
    print(name, "Your Grade is:", grade)

else:
    print(name, "You are Failed!")

