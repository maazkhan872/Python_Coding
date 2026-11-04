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
