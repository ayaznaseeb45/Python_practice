number = [6,7 ,1,3,2,5,4]

for i in range(len(number)):
    for j in range(len(number) - 1):
        if number[j] > number[j + 1]:
            number[j] , number[j + 1] = number[j + 1] , number[j]
    
print(number)