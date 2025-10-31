# Create a Module: To create a module just save the code you want in a file with the file extension .py:
#Example:
# Save this code in a file named mymodule.py
def greeting(name):
    print("Hello, " + name)

#Now we can use the module we just created, by using the import statement:
import mymodule
mymodule.greeting("Jonathan")