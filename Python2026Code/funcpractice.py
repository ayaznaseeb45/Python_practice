# # local variable 

# # def my_function():
# #     x = 10   # local variable

# # print(x)

# # Gloabal variable function 
# x = 10  
# def my_function():
#     print(x) 


# Write a function that takes any number of integers using *args and returns their sum.

# def sun_func(*args):
#     print(sum(args))
# sun_func(1,2,3)

# Write a function that accepts user details using **kwargs and returns them as a dictionary.
# import json
# def user_info(**kwargs):
#     print(json.dumps(kwargs, indent=4))

# user_info(name= "ayaz", clas = 2 , profession ="Engineer")


# Write a function that takes a list of numbers and returns only the even numbers.


def number(*args):
    even_list = []
    for n in args:
        if n % 2 == 0:
            even_list.append(n)
    return even_list



result = number(2,4,5)
print(result)