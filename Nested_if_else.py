# Check condition to eligible to vote
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult")

    if age >= 18:
        print("You are eligible to vote")

else:
    print("You are not eligible to vote")

# Login Problem
username = input("Enter username: ")

if username == "admin":

    password = input("Enter password: ")

    if password == "12345":
        print("Login Successful")

    else:
        print("Incorrect Password")

else:
    print("Invalid Username")

# Age and Card Problem
age = int(input("Enter your age: "))

if age >= 18:

    card = input("Do you have an admission card? ")

    if card == "yes":
        print("Admission Allowed")

    else:
        print("Admission Denied")

else:
    print("Age Requirement Not Met")

# ATM Withdrawal problem
balance = int(input("Enter your account balance: "))

if balance > 0:

    amount = int(input("Enter withdrawal amount: "))

    if amount <= balance:
        print("Withdrawal Successful")

    else:
        print("Insufficient Balance")

else:
    print("Invalid Account Balance")


# Student Grade problem
marks = int(input("Enter your marks: "))

if marks >= 50:

    if marks >= 80:
        
        if marks >= 90:
            print("Grade A")
        else:
            print("Grade B")

    else:
        print("Grade C")

else:
    print("Failed")


# Job Eligibility problem
age = int(input("Enter your age: "))

if age >= 18:

    education = input("Enter your education: ")

    if education == "Bachelor":
        print("Eligible for Job")

    else:
        print("Education Requirement Not Met")

else:
    print("Age Requirement Not Met")