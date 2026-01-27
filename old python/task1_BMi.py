# name = input("Enter Your Name: ")
# weight = float(input("Enter your weight: "))
# height = float(input("Enter your height: "))


# if weight <= 0 or height <= 0:
#     print("I think you entered wrong values.")
# else:
#     bmi = round(weight / (height ** 2))  
#     print(f"Mr. {name}, your BMI is: {bmi}")

#     # BMI classification
#     if bmi < 25:
#         print("You have a healthy weight.")
#     elif bmi >= 25 and bmi <= 30:  
#         print("You are overweight.")
#     else:
#         print("Obesity: Obesity is a condition that occurs when a person has excess weight or body fat that might affect their health.")



name = input("Enter Your Name: ")
weight = float(input("Enter your weight: "))
height_in_feet = float(input("Enter your height in feet: "))

# Convert height from feet to meters
height_in_meters = height_in_feet * 0.3048

# Check if weight or height is invalid
if weight <= 0 or height_in_meters <= 0:
    print("I think you entered wrong values.")
else:
    bmi = round(weight / (height_in_meters ** 2))  
    print(f"Mr. {name}, your BMI is: {bmi}")

    # BMI classification
    if bmi < 25:
        print("You have a healthy weight.")
    elif bmi >= 25 and bmi <= 30:  
        print("You are overweight.")
    else:
        print("Obesity: Obesity is a condition that occurs when a person has excess weight or body fat that might affect their health.")
