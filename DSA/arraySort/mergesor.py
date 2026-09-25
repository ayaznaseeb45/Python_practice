def merge_sort(arr):

    # Stop if array has 0 or 1 element
    if len(arr) <= 1:
        return arr

    # ==========================
    # Step 1: Divide the array
    # ==========================
    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    # ==========================
    # Step 2: Recursively sort
    # ==========================
    left = merge_sort(left)
    right = merge_sort(right)

    # ==========================
    # Step 3: Merge
    # ==========================
    return merge(left, right)


def merge(left, right):

    result = []

    i = 0
    j = 0

    # Compare both arrays
    while i < len(left) and j < len(right):

        # Take the smaller element
        if left[i] < right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    # Add remaining elements from left
    result.extend(left[i:])

    # Add remaining elements from right
    result.extend(right[j:])

    return result


numbers = [3, 1, 2, 4, 1, 5, 2, 6, 4]

print(merge_sort(numbers))