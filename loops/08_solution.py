# user entered number is prime or not 

is_prime =True
user_input = int(input("Enterd a Number: "))

if user_input > 1:
    for i in range(2, user_input):
        if user_input % i == 0:
            is_prime = False
            break
print(f"{user_input} is {is_prime} prime number ")