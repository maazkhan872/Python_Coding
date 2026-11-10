# Problem 1
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Problem 2
num = int(input("Enter a number: "))

if num > 0:
    print("Positive Number")
else:
    print("Negative Number")

# Problem 3
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# Problem 4
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("First number is greater")
elif num2 > num1:
    print("Second number is greater")
else:
    print("Both numbers are equal")

# Problem 5
password = input("Enter your password: ")

correct_password = "python123"

if password == correct_password:
    print("Login Successful")
else:
    print("Incorrect Password")

# Problem 6
marks = int(input("Enter your marks: "))

if marks >= 50:
    print("You are Passed")
else:
    print("You are Failed")

# Problem 7
marks = int(input("Enter your marks out of 100: "))

if marks >= 90 and marks <= 100:
    print("Grade: A+")
elif marks >= 80 and marks <= 89:
    print("Grade: A")
elif marks >= 70 and marks <= 79:
    print("Grade: B")
elif marks >= 60 and marks <= 69:
    print("Grade: C")
elif marks >= 50 and marks <= 59:
    print("Grade: D")
elif marks < 50 and marks >= 0:
    print("Fail")
else:
    print("Invalid Marks")

# Problem 8
num = int(input("Enter a number: "))

if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")

# Problem 9
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid Operator")

# Problem 10
temperature = float(input("Enter temperature: "))

if temperature > 35:
    print("Very Hot")
elif temperature >= 25:
    print("Hot")
elif temperature >= 15:
    print("Moderate")
elif temperature >= 5:
    print("Cold")
else:
    print("Very Cold")

# Problem 11
age = int(input("Enter your age: "))

if age < 5 and age >= 0:
    print("Free Ticket")
elif age <= 12:
    print("Child Ticket")
elif age <= 17:
    print("Teen Ticket")
elif age <= 59:
    print("Adult Ticket")
elif age >= 60:
    print("Senior Citizen Ticket")
else:
    print("Invalid Age")

# Problem 12
units = int(input("Enter consumed units: "))

if units >= 0 and units <= 100:
    bill = units * 10
    print("Electricity Bill: Rs.", bill)

elif units <= 200:
    bill = units * 15
    print("Electricity Bill: Rs.", bill)

elif units > 200:
    bill = units * 20
    print("Electricity Bill: Rs.", bill)

else:
    print("Invalid Units")

# Problem 13
age = int(input("Enter your age: "))
income = int(input("Enter your monthly income: "))

if age >= 21 and income >= 50000:
    print("You are eligible for the loan")
else:
    print("You are not eligible for the loan")

# Problem 14
amount = float(input("Enter total shopping amount: "))

if amount < 2000 and amount >= 0:
    discount = 0

elif amount < 5000:
    discount = amount * 0.05

elif amount < 10000:
    discount = amount * 0.10

else:
    discount = amount * 0.20

final_amount = amount - discount

print("Original Amount: Rs.", amount)
print("Discount: Rs.", discount)
print("Final Amount: Rs.", final_amount)

# Problem 15
gb = float(input("Enter internet usage in GB: "))

if gb < 5 and gb >= 0:
    print("Low Usage")

elif gb <= 20:
    print("Normal Usage")

elif gb <= 50:
    print("High Usage")

elif gb > 50:
    print("Very High Usage")

else:
    print("Invalid Usage")


# Problem 16
experience = float(input("Enter years of experience: "))
salary = float(input("Enter monthly salary: "))

if experience < 1 and experience >= 0:
    bonus = 0

elif experience <= 3:
    bonus = salary * 0.05

elif experience > 3 and salary < 100000:
    bonus = salary * 0.10

elif experience > 3 and salary >= 100000:
    bonus = salary * 0.15

else:
    bonus = 0

print("Monthly Salary: Rs.", salary)
print("Bonus Amount: Rs.", bonus)
print("Total Salary: Rs.", salary + bonus)