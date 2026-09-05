text = input("Enter text: ").lower()

non_repeating = []

for ch in text:
    if ch != " " and text.count(ch) == 1:
        non_repeating.append(ch)

if len(non_repeating) >= 2:
    print("Second non-repeating:", non_repeating[1])
else:
    print("Second non-repeating character nahi hai")

if non_repeating:
    print("Last non-repeating:", non_repeating[-1])
else:
    print("Koi non-repeating character nahi hai")