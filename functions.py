# def sum (a,b):
#     c = a + b
#     print(c)

# sum(10 , 20)

# def multi(a , b):
#     c = a * b 
#     print(c)

# multi( 10 ,)


# def multi(a , b):
#     c = a * b 
#     return f"result is {c}"

# a = multi( 10 , 5)
# print(a)

# def multi():
#     a = 10
#     b = 15
#     c= a * b 
#     return f"result is {c}"

# print(multi())


# def eve_odd():
#     num = int(input("Enter a number: "))

#     if num == 0:
#         print("Plz Enter a valid number")
#         num = int(input("enter a number: "))
#     if num % 2 ==0:
#         print("even")
#     else:
#         print("odd")
#     return f"the value is {num}"

# Value = eve_odd()
# print(Value)

# function to print triangle:

def lines():
    line = int(input("Enter number of lines = "))
    for i in range(1, line + 1):
        for j in range(i):
            print("*", end=" ")  
        print()  

    return f"The triangle with {line} lines has been created."

print(lines())
