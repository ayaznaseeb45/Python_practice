number = [6,7,1,3,2,5,4]

for i in range(1, len(number)):

    key = number[i]

    j = i - 1

    while j >=0 and number[j] > key:
        number[ j + 1] = number[j]
        j = j - 1

    # Put the current number in the correct place
    number [j + 1] = key

print(number)

