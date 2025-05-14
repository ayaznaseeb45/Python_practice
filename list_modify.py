# 1 append
# fruirts = ["apple", "banana", "cherry"]

# print(fruirts)

# # replace element at index 1 
# fruirts[1]="xoxo"
# print(fruirts)


# add element in list
# fruirts.append("azee")
# print(fruirts)
# fruirts.remove("azee")
# print(fruirts)

#2 extend

# fruirt = ["apple", "orange"]
# print(fruirt)
# new_fruits = ["mango", "cherry"]

# fruirt.extend(new_fruits)
# print(fruirt)


# 3 insert

# fruits = ["apple", "mango"]
# fruits.insert(1, "chuchu")
# print(fruits)

# 4 remove This will remove the first occuance
# fruits = ["apple", "mango", "apple", "cherry"]
# fruits.remove("apple")
# print(fruits)


# 5 clear
# fruits = ["apple", "mango", "apple", "cherry"]
# fruits.clear()
# print(fruits)


# 6 finding index 

# fruits = ["apple", "mango", "apple", "cherry"]
# index = fruits.index("apple")
# print(index)

# finding index with range
# fruits = ["apple", "mango", "apple", "cherry"]
# index = fruits.index("apple", 2)
# print(index)


# 7 count elements
# fruits = ["apple", "mango", "apple", "cherry"]
# count =fruits.count("apple")
# print(count)

# 8 reverse
# fruits = ["apple", "mango", "apple", "cherry"]
# fruits.reverse()
# print(fruits)

# # 9 sorting
# fruits = ["1", "2","3","4","5"]
# fruits.sort()
# print(fruits)
# fruits.sort(reverse=True)

# 10 pop
# numbers = ["10", "20", "30", "40", "50"]
# popped = numbers.pop(2)
# print(popped)
# print(numbers)

# numbers = ["10", "20", "30", "40", "50"]
# last = numbers.pop()
# print(last)
# print(numbers)

# 11
fruits = ["apple", "mango", "apple", "cherry"]
copy_fruits = fruits.copy()
print(copy_fruits)
copy_fruits.append("xoxo")
print(copy_fruits)
