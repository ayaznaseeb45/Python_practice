numbers = [10, 40, 20, 40, 30]

largest = numbers[0]
second_largest = None

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num != largest:
        if second_largest is None or num > second_largest:
            second_largest = num

print("Largest:", largest)
print("Second largest:", second_largest)