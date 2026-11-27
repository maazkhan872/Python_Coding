# Take a string and print its first and last chracter
text = input("Enter a string: ")

print("First character:", text[0])
print("Last character:", text[-1])

# Reversed
word = input("Enter a word: ")

reverse_word = word[::-1]
print("Reversed word:", reverse_word)

#
name = "Maaz Khan"

print("First 6 characters:", name[:6])
print("Last 9 characters:", name[-9:])
print("Index 2 to 7:", name[2:8])

# Every Second Character
text = input("Enter a string: ")
print("Every second character:", text[::2])

# Email Slicing and Indexing
email = input("Enter your email: ")

print("First 5 characters:", email[:5])
print("Username:", email[:email.index("@")])
print("Domain:", email[email.index("@") + 1:])

# Uppercase and Lowercase
name = input("Enter your full name: ")

print("Uppercase:", name.upper())
print("Lowercase:", name.lower())

# Replace String
text = "I love Java"

new_text = text.replace("Java", "Python")
print(new_text)

# List Indexing
subjects = ["Python", "AI", "ML", "NLP", "Computer Vision"]

print("First element:", subjects[0])
print("Third element:", subjects[2])
print("Last element:", subjects[-1])
print("Second last element:", subjects[-2])

# List Slicing
numbers = [10, 20, 30, 40, 50, 60, 70, 80]

print("First 4 elements:", numbers[:4])
print("Last 3 elements:", numbers[-3:])
print("Index 2 to 5:", numbers[2:6])

# Reverse a List
cities = ["Karachi", "Lahore", "Islamabad", "Peshawar"]

reverse_cities = cities[::-1]
print("Reversed list:", reverse_cities)

# Every Second element
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Every second element:", numbers[::2])

# Empty List and Append
products = []

product1 = input("Enter first product: ")
products.append(product1)

product2 = input("Enter second product: ")
products.append(product2)

product3 = input("Enter third product: ")
products.append(product3)
print("Final product list:", products)

# List Insert And Remove
skills = ["Python", "HTML", "CSS", "JavaScript"]

skills.insert(1, "Machine Learning")
skills.remove("HTML")
print("Updated skills:", skills)

# Sort Students Marks
marks = [78, 45, 92, 66, 88, 54]

marks.sort()

print("Ascending order:", marks)
marks.sort(reverse=True)
print("Descending order:", marks)
