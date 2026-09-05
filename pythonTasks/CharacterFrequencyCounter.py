sentence = input("Enter a sentence: ")

frequency = {}

for ch in sentence:
    if ch != " ":
        if  ch in frequency: 
            frequency[ch] = frequency[ch] + 1
        else:
            frequency[ch] = 1

print(frequency)