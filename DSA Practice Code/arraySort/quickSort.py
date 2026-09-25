# [7,3,8,2,5]

def quick_sort(arr):

    # chose a pivot 
    if len(arr) <=1:
        return arr

    pivot = arr[0]

    # divide the array
    left = [] 
    right = []

    for num in arr[1:]:
        if num < pivot:
            left.append(num)
        if num > pivot:
            right.append(num)

    # sort left right 
    left = quick_sort(left)
    right = quick_sort(right)

    # combine both 
    return left + [pivot] + right

numbers = [20,40,10,20]

sortedNum = quick_sort(numbers)
print(sortedNum)
