# calculate sum of even numbers up to given number n

user_num = int(input("Enter a number: "))

sum_even = 0  

for num in range(1, user_num + 1):  
    if num % 2 == 0:
        sum_even += 1 

print("Sum of even numbers up to", user_num, "is:", sum_even)