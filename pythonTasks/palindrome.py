text = input("Enter a word or sentence: ")

clean_text = ""

for ch in text:
    if ch != " ":
        clean_text = clean_text + ch

reverse = ""

for ch in clean_text:
    reverse = ch + reverse

if clean_text.lower() == reverse.lower():
    print(f"{text} is a palindrome.")
else:
    print(f"{text} is not a palindrome.")