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