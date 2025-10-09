# age group customization classify a person age group : Child (<13), teenager (13 - 19), Adult (20 - 59), Senior (60+)

age = int(input("enter your age: "))

if (age < 13):
    print("you are child ")
elif age < 20:
    print("teenager")
elif age < 60:
    print("you are adult")

else:
    print("you are senior")

