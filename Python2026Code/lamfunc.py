# my_numbers =  [1, 2, 3, 4, 5]

# def my_square(x):
#     return x *x 

# square = list(map(my_square, my_numbers ))
# print(square)



# my_numbers =  [1, 2, 3, 4, 5]

# square = list(map( lambda x: x**2, my_numbers))
# print(square) 


user_input = int(input("Enter a number: "))

is_even = lambda x: x % 2 == 0

if is_even(user_input):
    print("Even number")
else:
    print("Odd number")

