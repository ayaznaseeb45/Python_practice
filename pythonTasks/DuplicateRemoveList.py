list_value = [10, 20, 10, 30, 20, 40]

unique_value = []

dublicates = []

for num in list_value:
    if num not in unique_value:
        unique_value.append(num)


print(f"unique value is {unique_value}")
