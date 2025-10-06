# validate input ask user tto enter number entered nuber between 1 to 10 


while(True):
    user_input = int(input("Enter a number between 1 to 10: "))

    # if user_input >= 1 and user_input <= 10:
    if 1 <= user_input <=10:
        print("Thanks, The number you entered is: ", user_input)
        break
    else:
        print("try again")
    