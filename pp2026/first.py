# 1. Reverse a String (Using Loop)

# text = "Hello"

# reversed = ''

# for chr in text:
#     reversed = chr + reversed

# print(reversed)

# # 2. Check Palindrome

# text = input("Enter a string: ")

# reversed_text = text[::-1]

# if text == reversed_text:
#     print(f"{text} is palidrome")
# else:
#     print(f"{text} is not palindrome")


# 3. Find Largest Number

# list1 = []

# print("Enter 5 numbers:")

# for i in range(5):
#     num = int(input(f"Enter number {i + 1}: "))
#     list1.append(num)

# largest_num = list1[0]

# for num in list1:
#     if num > largest_num:
#         largest_num = num

# print("Largest number is:", largest_num)


# # 4. Find Smallest Number

# list1=[10,20,30,40,50]

# smallest = list1[0]

# for num in list1:
#     if num < smallest:
#         smallest = num

# print(smallest)


# # 5. Find Second Largest Number

# numbers = [5, 12, 8, 25, 10]

# largest = second = float("-inf")

# for num in numbers:
#     if num > largest:
#         second = largest
#         largest = num
#     elif num > second and num != largest:
#         second = num

# print(second)
# print(largest)

# 5. Find Second Largest Number take input from user 

# list1 = []
# print("Enter 3 values: ")

# for i in range(3):
#     numbers = int(input(f"Enter value { i + 1}: "))

#     list1.append(numbers)

# largest = second = float("-inf")

# for num in list1 :
#     if num > largest:
#         second = largest
#         largest = num
#     elif second > num and second != largest:
#         second = num
# print(second)


# 6. Count Vowels

# text = "FastAPi"

# count = 0

# for char in text:
#     if char.lower() in "aeiou":
#         count = count + 1 
# print(count)

# 7. Count Characters

# text = "Hello Ayaz"

# count = 0

# for char in text:
#     if char.strip():
#         count = count + 1 

# print(count)


# 8. Remove Duplicate Elements
# numbers = [1,2,2,3,4,4,5]
# # num = set(numbers)
# # print (num)

# result = []

# for num in numbers:
#     if num not in result:
#         result.append(num)

# print (result)


# 8. show Duplicate Elements
# numbers = [1,2,2,3,4,4,5]

# result = []
# dublicate = []

# for num in numbers:
#     if num not in result:
#         result.append(num)
#     else:
#         dublicate.append(num)


# print(dublicate)

# numbers = [1,2,2,3,4,4,5]

# dublicate = []

# for num in numbers:
#     if numbers.count(num) > 1 and num not in dublicate:
#         dublicate.append(num)

# print(dublicate)


# 9. show Duplicate char in text

# text = "Ayazz"

# dublicate = []
# count = 0
# for char in text:
#     if text.lower().count(char) > 1 and char not in dublicate:
#         dublicate.append(char)
#         count += 1

# print(f"total count {count} repeated cahr are {dublicate}")
# print(dublicate)
# print(count)


# 10. Fibonacci Series

# a = 0
# b = 1

# for i in range(10):
#     print(a, end=" ")
#     a, b = b , a + b


# 10. factorial
# number = int(input("Enter a number: "))

# fact = 1

# for i in range(number , 1 , -1):
#     fact = fact * i

# print(fact)

# 12. Prime Number

# num = int(input("Enter a number: "))

# if num <= 1:
#     print("not a prime")
# else:
#     for i in range(2 , num):
#         if num % i == 0:
#             print("not a prime")
#             break
#         else:
#             print("its a prime number")



# 13. Sum of List

# numbers = [10, 20, 30, 40]

# total = 0

# for num in numbers:
#     total = total + num

# print(total)


# # 15. Multiplication Table

# table = int(input("enter a number: "))

# for num in range(1 , 11):
#     print(f"{table} x {num}  =  {table * num} ")

# 13. Sum of digits 
# number = 12345

# total = 0

# while number > 0:
#     digit = number % 10
#     total = total + digit 
#     number = number // 10

# print(total)


# 14. Reverse a Number
# number = 12345

# reverse = 0

# while number > 0:
#     digit = number % 10
#     reverse = reverse * 10 + digit
#     number //= 10

# print(reverse)


# number = 12345
# revers = ""
# for num in str(number):
#     revers = num + revers

# print(type(revers))
# result = int (revers)
# print(type(result))


# 15. Count Digits
# number = 123456
# count = 0

# while number > 0:
#     count += 1
#     number //= 10

# print(count)


# 16. Check Armstrong Number

# number = int(input("Enter a number: "))

# digits = len(str(number)) 

# total = 0
# temp = number

# while temp > 0:
#     digit = temp % 10
#     total = total + digit ** digits
#     temp = temp // 10

# if total == number:
#     print("Armstrong")
# else:
#     print("Not Armstrong")


# 19. Sum of Even Numbers

# total = 0

# for i in range(1, 21):
#     if i % 2 == 0:

#         total = total + i

# print(total)


# numbers = [10, 20, 30, 40]

# target = int(input("Enter targer number: "))

# found = False

# for num in numbers:
#     if num == target:
#         found = True
#         print(f"'{target}' is \"found in the\" list' ")
#         break

# else:
#     print("not found")


# 22. Count Positive and Negative Numbers

# numbers = [10, -5, 20, -7, 15]

# positive_count = 0
# negative_count = 0

# for num in numbers:
#     if num > 0:
#         positive_count += 1
#     else:
#         negative_count += 1

# print(positive_count)
# print(negative_count)


# # 23. Find Maximum and Minimum in One Loop

# numbers = [12, 45, 2, 78, 34]

# maximum = numbers[0]
# minimum = numbers[0]

# for num in numbers:
#     if num > maximum:
#         maximum = num
#     if num < minimum:
#         minimum = num
# print(minimum)
# print(maximum)


# # 24. Character Frequency

# text = "banana"

# frequency = {}

# for char in text:
#     if char in frequency:
#         frequency[char] += 1
#     else:
#         frequency[char] = 1


# 25. Count Words

# sentence = "Python is easy and Python is powerful"

# words = sentence.split()

# counts = {}

# for word in words:
#     if word in counts:
#         counts[word] += 1
#     else:
#         counts[word] = 1

# print(counts)

# # 26. Bubble Sort
# numbers = [5, 3, 8, 1, 4]

# for i in range(len(numbers)):
#     for j in range(len(numbers) - 1):

#         if numbers[j] > numbers[j + 1]:
#             numbers[j] , numbers[j + 1] = numbers[j + 1], numbers[j]
#             # temp = numbers[j]
#             # numbers[j] = numbers[j + 1]
#             # numbers[j + 1] = temp

# print(numbers)


# 27. Selection Sort
# numbers = [5, 3, 8, 1, 4]

# for i in range(len(numbers)):

#     min_index = i

#     for j in range(i+1, len(numbers)):
#         if numbers[j] < numbers[min_index]:
#             min_index = j

#     numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

# print(numbers)


# 30. right align stars 

# for i in range(1, 6):
#     # print(" " * (5-i) + "*" * i)
#     print("*" * i, " " * (6 -1))


