
numbers = [5, 3, 8, 1, 4]
# 26. Bubble Sort
# for i in range(len(numbers)):
#     for j in range(len(numbers) -1):
#         if numbers[j] > numbers[j + 1]:
#             temp = numbers[j]
#             numbers[j] = numbers[j + 1]
#             numbers[j + 1] = temp
            
# print(numbers)

# 27. Selection Sort

for i in range(len(numbers)):
    min_index = i

    for j in range( 1 + i , len(numbers)):
        if numbers[j] < numbers[min_index]:
            min_index = j
        
    numbers[i] , numbers[min_index] = numbers[min_index], numbers[i]

print(numbers)