numbers = [2, 7, 11, 15]
target = 9

found = False

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print("Numbers are:", numbers[i], numbers[j])
            found = True
            break

    if found:
        break

if not found:
    print("No pair found")