# # # # # # # # values = []

# # # # # # # # for i in range(5):
# # # # # # # #     user_input =  input("enter a value ")
# # # # # # # #     values.append(user_input)

# # # # # # # # print(values)
# # # # # # # # print(reversed(values))


# # # # # # # student = {
# # # # # # #     "name" : "Ayaz",
# # # # # # #     "age" : 25, 
    
# # # # # # # }
# # # # # # # # students["name"] = "xyz"
# # # # # # # # students["city"] = "Lahore"

# # # # # # # # print(students)

# # # # # # # # del students["age"]
# # # # # # # # print(students)


# # # # # # # print(student.keys())
# # # # # # # print(student.values())
# # # # # # # print(student.items())

# # # # # # # print("name" in student.keys())

# # # # # # # print("salary" in student.keys())



# # # # # # student = {
# # # # # #     "name": "Ali",
# # # # # #     "age": 20,
# # # # # #     "city": "Lahore"
# # # # # # }

# # # # # # # for key, values in student.items():
# # # # # # #     print(f"key '{key}' has value '{values}'")

# # # # # # # print(student.items())



# # # # # sets= {10, 2, 43, 47, 5, 14}
# # # # # print(sets)


# # # # z = 2 + 3j

# # # # print(z)
# # # # print(z.real)
# # # # print(z.imag)



# # # # text = "            I love Pakistan          "
# # # # print(text)

# # # # # print(text.split())
# # # # print(text.strip())



# # # a = "green"
# # # mid_value = len(a) // 2   

# # # print("mid value: " , mid_value)

# # # result = a[mid_value]

# # # print("Middle character is:", result)



# # respose = {
# #     "hello":"hi how can i help you",
# #     "hi": "hello how are u today" 
# # }


# # def chatBot(user_question):
# #     user_question = user_question.lower().strip()

# #     for key , value in respose.items():
# #         if key in user_question:
# #             return value
# #     return "I am still learning"

# # user_input = input("how can i help you?: ")

# # reply = chatBot(user_input)
       
# # print(reply)



# response  = {
#     "hello": "Hi! Welcome. How can I help you today?",
#     "hi": "Hello! Nice to see you.",
#     "how are you": "I'm doing great, thank you for asking!",
#     "who are you": "I am KotliBot, a smart AI assistant created to help you.",
#     "what is your name": "My name is KotliBot.",
#     "what can you do": "I can help you with basic questions, coding guidance, and simple conversations.",
#     "thank you": "You're welcome! Happy to help.",
#     "bye": "Goodbye! Have a great day.",
#     "happy": "Keep going! Every bug in your project makes you a better developer.",
#     "function kya hota hai": "A function is a reusable block of code that performs a specific task."
# }

# def get_response(user_question):
#     user_question = user_question.lower().strip()

#     for key , value in response.items():
#         if key in user_question:
#             return value 
#     return "I am still learning about that.."

# user_input = input("Please ask your question: ")
# reply = get_response(user_input)
# print(reply )    

# ---------------------------- interview_questions = 

# list vs tuple 

# list1 = [10, 20, 30, 40, 50]
# list1[1] = 25
# print(list1)

# tuple1 =(10, 20, 30, 40, 50)
# # tuple1[1] = 25 


# set vs list 

# text = "Hello"
# txt =text.replace("H", "Y")
# print(txt)


# a = [1, 2, 3]
# b = a

# b.append(4)

# print(a)



# user_input = int(input("Enter a number: "))

# if user_input % 2 == 0:
#     print("Even")
# else:
#     print("Odd")    


# username = "login"
# password = "12345"
# counter = 0
# while True:
#     user_input_username = input("Enter username: ")
#     user_input_password = input("Enter password: ")
#     counter += 1
#     print(f"Attempt {counter}:")
#     if user_input_username == username and user_input_password == password:
#         print("Login successful!")
#         break
#     else:
#         print("Invalid username or password. Please try again.")
        



# a = 10
# b = 20
# c= 30 

# arr = [a, b, c]

# for i in range(1):
#     temp = arr[0]
#     arr[0] = arr[1]
#     arr[1] = arr[2]
#     arr[2] = temp

#     a, b, c = arr
# print("a:", a)
# print("b:", b)      
# print("c:", c)



# user_input = int(input("Enter a number: "))


# if user_input <= 1:
#     print("Not a Prime Number")


# else:
#     is_prime = True
#     for i in range(2 , user_input):
#         if user_input % i == 0:
#             print ("Not a Prime Number")
#             break
#     if is_prime:
#         print("Prime Number")
#     else:
#         print("Not a Prime Number")


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




# num = int(input("Enter a number: "))

# # Even / Odd check
# if num % 2 == 0:
#     print("Even Number")
# else:
#     print("Odd Number")

# # Prime check
# if num <= 1:
#     print("Not a Prime Number")
# else:
#     is_prime = True

#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print("Prime Number")
#     else:
#         print("Not a Prime Number")


# user_input = int(input("Enter a number: ")) 


# even odd check 

# if user_input % 2 == 0:
#     print("Even Number")
# else:
#     print("Odd Number")

# # Prime check 

# if user_input <= 1:
#     print("Not a Prime Number")
# else:
#     is_prime = True
#     for i in range (2, user_input):
#         if user_input % i == 0:
#             print("Not a Prime Number")
#             is_prime = False
#             break
#     if is_prime:
#         print("Prime Number")
#     else:
#         print("Not a Prime Number")



# num = int(input("Enter a number: "))

# print("\nWhat do you want to check?")
# print("1. Even or Odd")
# print("2. Prime or Not Prime")

# choice = int(input("Enter your choice (1 or 2): "))

# # Even / Odd check
# if choice == 1:
#     if num % 2 == 0:
#         print("Even Number")
#     else:
#         print("Odd Number")

# # Prime check
# elif choice == 2:
#     if num <= 1:
#         print("Not a Prime Number")
#     else:
#         is_prime = True

#         for i in range(2, num):
#             if num % i == 0:
#                 is_prime = False
#                 break

#         if is_prime:
#             print("Prime Number")
#         else:
#             print("Not a Prime Number")

# else:
#     print("Invalid Choice")




# for i in range(1, 5):
#     for j in range (1, i + 1):
#         print("*", end="")
#     print()

# total = 0
# for i in range(1, 11):
#     total += i  
# print(total)

# list1 = [10, 20, 30, 40]
# # result = list1[::-1]
# reversed(list1)
# print(list1)



# a = [ "1", "2", "3", "4" ,"5"]
# x =[]
# for i in range(len(a)-1, -1, -1):
#     x.append(a[i])

# print(x)


# for i in range ( 5):
#     print(i * "*")

for i in range(5, 0, -1):
    print("*" * i)
