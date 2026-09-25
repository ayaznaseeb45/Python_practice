def selection_sort(arr):

    for i in range(len(arr)):

        min_index = i

        for j in range(i + 1 , len(arr)):
            if arr[j] < arr[min_index]:
                arr[j], arr[min_index] = arr[min_index], arr[j]

    return arr

num = [ 30, 10 , 20 , 40 ]

result = selection_sort(num)
print(result)