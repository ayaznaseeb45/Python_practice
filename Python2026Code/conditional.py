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

# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap year")
# else:
#     print("Not a leap year")    



# 8️⃣ Simple Login System

# username = input("Enter username: ")
# password = input("Enter password: ")

# if username == "admin" and password == "1234":
#     print("Login successful")
# elif username == "admin":
#     print("Wrong password")
# else:
#     print("User not found")


# Write a program to calculate an electricity bill based on units consumed.
# units_Consumed = int(input("enter unit consumed: "))
# price_of_unit = 3

# total_bill = price_of_unit * units_Consumed

# print(f"Total bill is {units_Consumed} Units is: ",total_bill)


#10 Write a program to check whether a number is a palindrome or not.

# num = input("Enter a number: ")

# if num == num[::-1]: 
#     print("The number you entered is a palindrome", num)
# else:
#     print("The number is not a palindrome")



# Triangle Validity Check

# a = int(input("Enter side 1: "))
# b = int(input("Enter side 2: "))
# c = int(input("Enter side 3: "))


# if a + b > c and b + c > a and c + a > b:
#     print("its valid triangle: ")

# else:
#     print("not valid triangle: ")


# calculator 

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# op = input("Enter operator (+, -, *, /): ")

# if op == "+":
#     print(a + b)
# elif op == "-":
#     print(a - b)
# elif op == "*":
#     print(a * b)
# elif op == "/":
#     print(a / b)
# else:
#     print("Invalid operator")



# # check number is prime or not 
# num = int(input("Enter a number: "))

# if num <= 1:
#     print("Not a Prime Number")
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not a Prime Number")
#             break
#     else:
#         print("Prime Number")


# match statement in python 

# num = 5

# match num:
#     case 1:
#         print("One")
#     case 2:
#         print("Two")
#     case 3:
#         print("Three")
#     case _:
#         print("Other number")




# day = int(input("Enter day number (1-7): "))  
# match day:
#     case 1:           
#         print("Monday")
#     case 2:   
#         print("Tuesday")

#     case 3:   
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")

#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Invalid day number")


