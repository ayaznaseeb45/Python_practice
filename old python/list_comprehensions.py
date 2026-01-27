#  Syntax reminder: list_name = [expression   for item in iterable     if condition]





#  List of squares
squares = [x**2 for x in range(1, 6)]  
print("Squares:", squares)




#  Even numbers from 1 to 5
even_list = [x for x in range(1, 6) if x % 2 == 0]
print("Even numbers:", even_list)






#  (uppercase fruits)
my_list = ['apple', 'mango', 'cherry']
print("Uppercase fruits:", end=" ")
for x in my_list:
    print(x.upper(), end=" ")
print()  





# Flatten a nested list using list comprehension
nested_list = [[1, 2], [3, 4], [5, 6]]
result = [item for sublist in nested_list for item in sublist]
print("Flattened using list comprehension:", result)

# 
import itertools
result = list(itertools.chain.from_iterable(nested_list))  # Correct way
print("Flattened using itertools:", result)

#  Flatten with function
def flaten_list(lst):
    return [item for sublist in lst for item in sublist]

final_list = flaten_list(nested_list)
print("Flattened using function:", final_list)
