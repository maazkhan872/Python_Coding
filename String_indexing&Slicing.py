# Python Indexing
name = "Python"

print(name[0])  # P
print(name[1])  # y
print(name[2])  # t
print(name[3])  # h
print(name[4])  # o
print(name[5])  # n


words = "Python"
print(words[-1])
print(words[-2])
words[-3]

# Slicing
name = "Programming"
print(name[0:4])

word = "Python"

print(word[0:3])  # Pyt
print(word[2:5])  # tho
print(word[1:4])  # yth

# Sentence Analyzer
sentence = input("Enter a sentence: ")

print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Count of a:", sentence.lower().count("a"))
print("Replace spaces:", sentence.replace(" ", "-"))
print("First 5 characters:", sentence[:5])

# Password Analyzer
password = input("Enter your password: ")

has_digit = any(char.isdigit() for char in password)
has_uppercase = any(char.isupper() for char in password)

if len(password) >= 8 and has_digit and has_uppercase:
    print("Strong password")
else:
    print("Weak password")