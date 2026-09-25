def bub_sort(arr):

    # Step 1: One element is already sorted
    if len(arr) <= 1:
        return arr

    # Step 2: Repeat passes
    for i in range(len(arr)):

        # Step 3: Compare adjacent elements
        for j in range(len(arr) - 1 - i):

            # Step 4: Swap if left is greater
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


numbers = [7, 2, 5, 4]

result = bub_sort(numbers)

print(result)