# print("Enter 2 value to check which one is greater: ")

# num1 = input("enter a num1 number: ")
# num2 = input("enter a num2 number: ")

# greater_value = "num 1 is greater " if num1>num2 else "num 2 is greater "
# print(greater_value)

# if num1 > num1:
#     print("num1 is greater: ")

# else:
#     print("num2 is greater: ")



# a= 35
# b = 10
# if a > b + 10:
#     print("a is greater than b by more than value 10")
# elif a > b:
#     print("a is greater")
# else:
#     print("b is greater")


# a = int(input("Enter num 1: "))
# b = int(input("Enter num 2: "))

# if a > b:
#     if a > b + 10:
#         print("a is greater than b by more than 10.")
#     else:
#         print("a is greater than b but by less than or equal to 10.")
# elif a == b:
#     print("a is equal to b.")
# else:
#     print("b is greater than a.")


a = int(input("Enter num 1: "))
b = int(input("Enter num 2: "))

if a > b:
    if a > b + 10:
        print("a is greater than b by more than 10.")
    else:
        print("a is greater than b but by less than or equal to 10.")
else:
    if a == b:
        print("a is equal to b.")
    else:
        print("b is greater than a.")

a = 2
b = 330
print("A") if a > b else print("B")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


# The and keyword is a logical operator, and is used to combine conditional statements:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# The or keyword is a logical operator, and is used to combine conditional statements:
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")


# The not keyword is a logical operator, and is used to reverse the result of the conditional statement:
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

