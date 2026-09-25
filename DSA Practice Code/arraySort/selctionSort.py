number = [20,10,50,40,30]


for i in range (len(number)):
    min_index = i 

    for j in range( i + 1 , len(number)):
        if number[j] < number[min_index]:
            min_index = j 
    number[i] , number[min_index] = number[min_index], number[i]    

print(number)