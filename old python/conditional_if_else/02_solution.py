# Movie ticket pricing are priced based on age : $12 for adults (18 and over), $8 for children. Everyone get a $2 discount on wednesday

age = 2
day = "wednesday"

price = 12 if age >= 18 else 8
if day == "wednesday":
    price =price - 2

print(price)
