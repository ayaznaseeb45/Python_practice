def insertion_sort(arr):
    if arr <=1:
        return arr 

    for i in range(1 , len(arr)):
        j = i - 1 
        