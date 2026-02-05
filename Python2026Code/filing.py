# file = open("dummy.txt", "r")
# data = file.read()
# print(f"data of file is: \n\n",data)


# file = open("certificate.txt", "r")
# data = file.read().lower()
# file.close()

# count = 0

# for word in data.split():
#     print(word)
#     if word == "alive":
#         count += 1

# if count > 0:
#     print("Yes, 'alive' is present in the file")
#     print(f"'alive' appeared {count} time(s) in the file")
# else:
#     print("'alive' is not available in the file")



# with open("myFile.txt", "a") as file:
#     file.write("\nwe are developers")

# with open("myFile.txt", "r") as file:
#     print(file.read())


# with open("ayz.txt", "w") as file:
#     print(file.write("we are devleoper"))

# with open("ayaz.txt", "r") as xoxo:
#     print(xoxo.read())


# file = open("test.txt", "x")
# file.write("this is my new file")
# file.close()
# print("file created successfully")


# with open("test.txt", "r") as file:
#     for xx in file:
#         print(xx.strip())

# with open ("test.txt", "r") as file:
#     for x in file:
#         print(x.strip(), end="")
#         break


# with open("test.txt", "r") as file:
#     count = 0
#     for x in file:
#         count += 1
#     print("total lines are ",count)


import os 

os.rename("test.txt", "khushi.txt")
