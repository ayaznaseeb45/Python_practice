text = input("Enter text: ").lower()

vowels = 0
consonants = 0

for ch in text:
    if ch in "aeiou":
        vowels = vowels + 1
    elif ch.isalpha():
        consonants = consonants + 1

print("Vowels:", vowels)
print("Consonants:", consonants)