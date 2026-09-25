x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


# You can get the data type of a variable with the type() function.
x = 5
y = "John"
print(type(x))
print(type(y))


# String variables can be declared either by using single or double quotes:

x = "John"
# is the same as
x = 'John'

# Variable names are case-sensitive.

a = 4
A = "Sally"
#A will not overwrite a


# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# And you can assign the same value to multiple variables in one line
x = y = z = "Orange"
print(x)
print(y)
print(z)


# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# you output multiple variables, separated by a comma:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)


# You can also use the + operator to output multiple variables:
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)


# In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
# x = 5
# y = "John"
# print(x + y)



# Global Variables Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()




# Create a variable inside a function, with the same name as the global variable

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# Python is fantastic
# Python is awesome


# If you use the global keyword, the variable belongs to the global scope:
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)