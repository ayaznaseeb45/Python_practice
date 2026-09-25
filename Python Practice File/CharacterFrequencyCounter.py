# sentence = input("Enter a sentence: ")

# frequency = {}

# for ch in sentence:
#     if ch != " ":
#         if  ch in frequency: 
#             frequency[ch] = frequency[ch] + 1
#         else:
#             frequency[ch] = 1

# print(frequency)


sentence = input("Enter a sentence: ")
freq = {}

for ch in sentence:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)
