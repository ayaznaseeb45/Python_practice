
# def check_guess(num, guess):
#     while guess != num:
#         guess = int(input("Enter a number between 1 to 10: "))
#         if guess != num:
#             print("You entered a wrong number. Try again!")
    
#     print("You guessed right!")

# # Call the function with arguments
# check_guess(9, 0)


num = 9
guess = 0
attempts = 0
max_attempts = 3

while guess != num and attempts < max_attempts:
    guess = int(input("Enter a number between 1 to 10: "))
    attempts += 1
    
    if guess != num:
        print(f"You entered a wrong number. Try again! ({attempts}/{max_attempts})")

if guess == num:
    print("You guessed right!")
else:
    print("Attempts ended.")