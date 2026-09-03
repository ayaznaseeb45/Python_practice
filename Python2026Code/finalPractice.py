# n = int(input("Enter number: "))
# total = 0

# for i in range(1, n+1):
#     total += i

# print(total)



# user_input = int(input("Enter a number: ")) 

# if user_input <= 1:
#     print("Not a Prime Number")
# else: 
#     is_prime = True
#     for i in range(2, user_input):
#         if user_input % i == 0:
#             print("Not a Prime Number")
#             break
#     if is_prime:
#         print("Prime Number")
#     else:
#         print("Not a Prime Number")

# user_input = int(input("Enter a number: "))

# if user_input <= 1:
#     print("not a prime number")
# else:
#     is_prime = True
#     for i in range (2, user_input):
#         if user_input % i == 0 :
#             print("not a prime number")
#     if is_prime:
#         print("its a prime number")
#     else:
#         print("not a prime number")




# user_input = int(input("Enter a number: "))


# # check even and oddd 
# if user_input % 2 == 0:
#     print("Even number")
# else:
#     print(" its odd number")

# # check prime num

# if user_input <=1:
#     print("not a prime number")
# else:
#     is_prime = True
#     for i in range(2, user_input):
#         if user_input % 2 ==0:
#             is_prime = False
#             break
#     if is_prime:
#         print("its prime number")
#     else: 
#         print("not a prime number ")


# user_input = int(input("enter user input: "))


# fact = 1
# for i in range(1, user_input + 1):
#     fact = fact * i

# print(fact)


# nums = [3, 7, 2, 9]


# max_num = nums[0]

# for i in nums:
#     if i > max_num:
#         max_num = i

# print(max_num)

# text = input("Enter string: ")

# rev = ""

# for ch in text:
#     rev = ch + rev

# print(rev)


# num = [1,2,3,4,5]

# z= []

# for i in num :
#     x = i * i 
#     z.append(x)

    




# num = input ("enter number : ")

# rev = ""

# for i in num:
#     rev = i + rev

# print(rev)

# for i in range (5, 0, -1):
#     print(i * "*")



# n = input("enter a number ")

# a = 0
# b = 1

# for i in range(n):
#     print(a)
#     c = a + b
#     a = b
#     b = c

text = input("enter")

rev = ""

for i in text:
    rev = i + rev

print(rev)