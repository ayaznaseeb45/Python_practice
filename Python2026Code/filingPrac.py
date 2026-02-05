# file = open ("data.txt", "w")
# data = file.write("python file handling")
# print(data)

# with open("data.txt", "r") as file:
#     for data in file:
#         print(data.strip())


# with open("data.txt", "a") as file:
#     file.write("Learning never stops\n")


# try:
#     with open("log.txt", "x") as file:
#         file.write("Log started\n")
# except FileExistsError:
#     print("File already exists")

# import shutil

# shutil.copy("data.txt", "data_backup.txt")


with open ("data.txt", "r") as srcFile:
    content = srcFile.read()
    if content:
        with open("summary.txt", "w") as newFile:
            newContent = newFile.write(content)
    else:
        print("not working")