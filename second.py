# this is about Python Variables

'''
A variable can have a short name (like x and y) or a more descriptive name
 (age, carname, total_volume).

Rules for Python variables:

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.

'''

x = 10
y = "Hello, World!" 
print(x)
print(y)

X = 500
Y = "doing a python is just fun"

print(X)
print(Y)


# Assign Multiple Values

x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)


car = ["lamborgini", "bmw", "omni"]
x, y, z = car

print(z)
print(x)
print(y)


# Global Variables

'''
Variables that are created outside of a function 
(as in all of the examples in the previous pages) are known as global variables.
'''
# outside function

y = "great"

def my_self():
    print("Samir is " + y)

my_self()


# Local Variables

y = "awesome"

def my_function():
    y = "good"
    print("samir is " + y)

my_function()
print("samir is " + y)


# Changing Global Variables

y = "beautiful"

def my_car():
    global y
    y = "fantastic"

my_car()
print("BMW is " + y)