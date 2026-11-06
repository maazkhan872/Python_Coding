# Calculate Rectangle Area
length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width

print("Rectangle Area =", area)

# Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Fahrenheit =", fahrenheit)

# Even or Odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# Grading System
marks = int(input("Enter a marks:"))

if marks >= 90:
    print("Got A+ grade")
elif  marks >= 80:
    print("Got A grade")
elif  marks >= 70:
    print("Got B grade")
elif  marks >= 60:
    print("Got C grade")
elif  marks >= 50:
    print("Got D grade")
else:
    print("You are failed!")


# Voting Eligibility
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible for voting")

else:
    print("Not eligible for voting")


# Find Greater Between Two Numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("First number is greater")

elif num2 > num1:
    print("Second number is greater")

else:
    print("Both numbers are equal")