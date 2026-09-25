# factorial question using for loop:

# num = int(input("Enter a number: "))
# fact = 1

# for i in range(1, num + 1):
#     fact = fact * i  

# print("Factorial of", num, "is", fact)


# factorial question using for loop:
num = int(input("Enter a number: "))
fact = 1
count =0
while(num > 0):
    fact = fact * num
    num = num -1
    count = count +1
print(f"Factorial {count} is: ", fact)