num = int(input("Enter a number: "))

if num <= 0:
    print("Please enter a positive integer")

elif num == 1:
    print("1 is not a prime number")

else:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("This is a prime number")
    else:
        print("This is not a prime number")