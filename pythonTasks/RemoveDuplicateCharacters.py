word = input("Enter a word: ")

result = ""

for ch in word:
    if not ch in result:
        result = result + ch


print("Word after removing duplicate characters:", result)