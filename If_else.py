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


# Find Greatest of Three Numbers
var_1 = int(input("Enter 1st number:"))
var_2 = int(input("Enter 2nd number:"))
var_3 = int(input("Enter 3rd number:"))

if var_1 >= var_2 and var_1 >= 3:
    print("Variable 1 is greater")
elif var_2 >= var_1 and var_2 >= var_3:
    print("Variable 2 is greater")
elif var_3 >= var_1 and var_3 >= var_2:
    print("Variable 3 is geater")
else:
    print("Not Possible")


# Divisible By 5 
number = int(input("Enter a number"))

if number % 5 == 0:
    print("Number is divisible by 5")
else:
    print("Number is not divisible by 5")


# Calculate Profit & Loss
cost_price = float(input("Enter cost price: "))
selling_price = float(input("Enter selling price: "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("Profit =", profit)

elif selling_price < cost_price:
    loss = cost_price - selling_price
    print("Loss =", loss)

else:
    print("No Profit No Loss")


# Electricity Bill Calculator
units = int(input("Enter electricity units: "))

if units < 0:
    print("Invalid units")

elif units <= 100:
    bill = units * 5
    print("Total Bill: Rs.", bill)

elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 8)
    print("Total Bill: Rs.", bill)

else:
    bill = (100 * 5) + (100 * 8) + ((units - 200) * 10)
    print("Total Bill: Rs.", bill)


# Whether a Number Is Divisible by 5 and 11
num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both")

# Leap Year or Not
year = int(input("Enter year: "))

if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not a Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")