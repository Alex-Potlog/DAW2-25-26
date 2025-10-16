# Basic Python Commands

# Print statement
print("Hello, World!")

# Variables and data types
x = 10          # Integer
y = 3.14        # Float
name = "Alice"  # String
is_active = True  # Boolean

# Basic arithmetic operations
a = 5
b = 2
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

# Conditional statements
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

# Loops
# For loop
for i in range(5):
    print("For loop iteration:", i)

# While loop
count = 0
while count < 5:
    print("While loop count:", count)
    count += 1

# Functions
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# Lists
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print("Fruits:", fruits)

# Dictionaries
person = {"name": "Alice", "age": 25, "city": "New York"}
print("Person's name:", person["name"])

# Sets
unique_numbers = {1, 2, 3, 3, 4}
print("Unique numbers:", unique_numbers)

# Tuples
coordinates = (10, 20)
print("Coordinates:", coordinates)

# Exception handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# File handling
with open("example.txt", "w") as file:
    file.write("This is a sample file.")

# Classes and objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

person = Person("Alice", 25)
print(person.introduce())