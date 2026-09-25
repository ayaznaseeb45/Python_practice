# numbers = [0, 1, 0, 3, 12]

# result = []

# zero = 0

# for num in numbers:
#     if num == 0:
#         zero = zero + 1
#     else:
#         result.append(num)
# for i in range(zero):
#     result.append(0)
# print(result)



numbers = [0, 1, 0, 3, 12]

result = []

zero = []

for num in numbers:
    if num == 0:
        zero.append(num)
    else:
        result.append(num)

result = result + zero

print(result)