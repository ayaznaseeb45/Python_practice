# write a function that takes a lits of string and return the count of vowels and consonents seperately.

def count_vowels_consonants(userInput):
    vowels = "aeiouAEIOU"
    vowels_list = []
    consonants_list = []

    for char in userInput:
        if char.isalpha():
            if char in vowels:
                vowels_list.append(char)
            else:
                consonants_list.append(char)

    print("Vowels:", vowels_list)
    print("Total vowels:", len(vowels_list))
    print("Consonants:", consonants_list)
    print("Total consonants:", len(consonants_list))


count_vowels_consonants("ayaz")
