# 1 Write a program to check whether a number is even or odd.

# num = int(input("Enter a number: "))

# if (num % 2 == 0):
#     print("Even")
# else:
#     print(" odd ")


# 2 Write a program to check whether a number is positive, negative, or zero.

# num = int(input("Enter a number: "))
# if (num > 0):
#     print("Positive: ")

# elif (num < 0):
#     print("num is negative")

# else:
#     print("Zero")


# 3 Write a program to check whether a person is eligible to vote (age ≥ 18).
# age = int(input("Enter your age: "))

# if age >= 18:
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote")


# 🟡 INTERMEDIATE LEVEL

# Write a program to find the largest of two numbers.

# a = int(input("Enter First number: "))
# b = int(input("Enter Second number: "))

# if (a > b):
#     print(" 'a' is greater")

# elif(b>a):
#     print("'b' is greater")

# else:
#     print("both are equal")




# Largest of Three Numbers
# a = int(input("enter first number: "))
# b = int(input("enter second number: "))
# c = int(input("enter third number: "))

# if (a > b and a > c):
#     print(" 'a' is greater ")

# elif(b > a and b>c ):
#     print("B is greater")

# else:
#     print("c is greater")

# print("the greater value is: ", max(a,b,c))



# Leap year calculator 

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")    
