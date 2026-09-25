# def add(x,y):
#     return x + y
# print(add(2,4))



# # function for intersection 

# list1=[1,2,3,4,5]
# list2=[4,5,6,7]

# def intersection_funct(list1, list2):
#     return [item for item in list1 if item in list2]


# print(intersection_funct(list1, list2))

# # fin the most repeated element in the list 


# num = [1,2,3,3,3,4,4,5,6]
# def most_freq(lst):
#     max_count = 0
#     most_freq = None
#     for item in lst:
#         count = list.count(item)
#         if count > max_count:
#             max_count = count
#             most_freq = item
#     return most_freq



# # second-way to solve it 
# num = [1, 2, 3, 3, 3, 4, 4, 5, 6]

# def most_freq(lst):
#     return max(set(lst), key=lst.count)

# print(most_freq(num))  


# remove dublicate from the list 
fruits = [ "apple", "banana", "cherry", "apple", "mango"]

def remove_dublication(list):
    return(set(list))

print(remove_dublication(fruits))   