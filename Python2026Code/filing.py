# file = open("dummy.txt", "r")
# data = file.read()
# print(f"data of file is: \n\n",data)


file = open("certificate.txt", "r")
data = file.read().lower()
file.close()

count = 0

for word in data.split():
    print(word)
    if word == "alive":
        count += 1

if count > 0:
    print("Yes, 'alive' is present in the file")
    print(f"'alive' appeared {count} time(s) in the file")
else:
    print("'alive' is not available in the file")
