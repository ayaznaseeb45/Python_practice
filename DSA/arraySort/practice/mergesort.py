

def merge_Sort(arr):

    if len(arr) <=1:
        return arr 
    mid = arr // 2 

    left = arr[:mid]
    right = arr[mid:]

    left = merge_Sort(left)
    right = merge_Sort(right)

    return merge(left, right)


def merge (left, right):
    result = []

    i = 0 
    j = 0 

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
        else: