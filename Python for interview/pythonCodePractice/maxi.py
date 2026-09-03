# # average of total num 
# numbers = [10, 20, 30, 40]

# total = 0
# count = 0
# for num in numbers:
#     total = total + num
#     count = count + 1

# result = total / count
# print(result)


# sum of even 
# number = [1,2,3,4,5,6]
# even_sum = 0
# for num in number:
#     # print(num)
#     if num % 2 == 0:
#         even_sum += num

# print (even_sum)\

# square of list 

# numbers = [1, 2, 3, 4, 5]

# square = [x ** 2 for x in numbers]
# print(square)


# count element kitni bar repeat howa ha count 

# numbers = [ 1, 2, 2 ,3 ,3 , 3, 4, 4, 4, 4, 5]

# count = {}

# for num in numbers:
#     if num in count:
#         count[num] += 1
#     else:
#         count[num] = 1

# print (count)


# # get odd index values 
# numbers = [10, 20, 30, 40, 50]

# odd_index_values = []

# for index in range(len(numbers)):
#     if index % 2 != 0:
#         odd_index_values.append(numbers[index])

# print(odd_index_values)


# # prime number 

# num = int(input("Enter a number: "))

# is_prime = True

# if num < 2 :
#     is_prime = False

# else:
#     for value in range(2, num):
#         if num % value == 0:
#             is_prime = False
#             break;

# if is_prime:
#     print(num, " is a prime number")
# else:
#     print(num, "is not a prime number")
    


# sort a list from low to high 

# num = [ 5,2,4,1,3]

# for i in range(len(num)):
#     for j in range(len(num) -1):
#         if num[j] < num[j + 1]:
#             num[j + 1] , num[j] = num[j], num[j + 1]
# print(num)



# remove dublicate value from arary 

# numbers = [1, 2, 2, 3, 1, 4, 3]

# new_num = []

# for num in numbers:
#     # print(num)
#     if not num in new_num:
#         new_num.append(num)


# print(new_num)


# numbers = [10, 45, 20, 80, 35]

# largest = numbers[0]

# for num in numbers:
#     if num > largest:
#         largest = num

# print(largest)


# numbers = [10, 45, 20, 80, 35]

# # Find largest number
# largest = numbers[0]

# for num in numbers:
#     if num > largest:
#         largest = num

# # Find second-largest number
# second_largest = None

# for num in numbers:
#     if num != largest:

#         if second_largest is None:
#             second_largest = num

#         elif num > second_largest:
#             second_largest = num

# print("Largest:", largest)
# print("Second largest:", second_largest)
            



# reverse a string 
# word = input("enter a word: ")

# reverse = "" 

# for ch in word:
#     reverse = ch + reverse

# print (reverse)




# what is palindrom 

# user_input = input("Enter a word: ").lower()

# reverse = ""

# for char in user_input:
#     reverse = char + user_input

# # print(reverse)

# if user_input == reverse:
#     print("its palindrome")

# else:
#     print("its not palindrome")


# count vowels
# user_input = input("Enter a word: ").lower()
# count = 0


# for char in user_input:
#     # print(char)
#     if char in "aeiou":
#         count += 1

# print(count)



# # remove dublicate 
# word = input("Enter a word: ")
# result = ""

# for char in word :
#     if char not in result:
#         result = result + char

# print(result)

# sentence = input("Enter a sentence: ")

# result = ""

# for ch in sentence:
#     if ch != " ":
#         result = result + ch

# print("Without spaces:", result)

# numbers = [1, 2, 2, 3, 1, 4, 3]

# unique_numbers = []

# for num in numbers:
#     if num not in unique_numbers:
#         unique_numbers.append(num)

# print(unique_numbers)



# # find the target value 
# numbers = [10, 20, 30, 40, 50]


# target = int(input("Enter a value: "))
# found = False


# for index in range(len(numbers)):
#     if numbers[index] == target:
#         found = True
#         print(index)
#         break

# if found == False:
#     print("no value founded ")


numbers = [10, 20, 30, 40, 50]
target = 40

start = 0
end = len(numbers) - 1

while start <= end:
    mid = (start + end) // 2

    if numbers[mid] == target:
        print("Number found at index:", mid)
        break

    elif target > numbers[mid]:
        start = mid + 1

    else:
        end = mid - 1