# print the multiplication table for the given number up to 10. but skip the fifth one 

user_input = int(input("Enter a number: "))


for i in range(1, 10):
    if (i == 5):
        continue
    print(user_input, "x" , i ,"=", user_input*i)
    
   
    
   