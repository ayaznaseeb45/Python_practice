# Basic Concepts of File Handling in Python

# 1️ Write Mode ('w')
# -> Creates a new file if it doesn’t exist
# -> Overwrites the content if file already exists

file = open('example.txt', 'w')
file.write("Hello, this is write mode.\n")
file.close()


# 2️ Read Mode ('r')
# -> Used to read data from a file
# -> File must already exist, otherwise error

file = open('example.txt', 'r')
content = file.read()
print("Reading file content:")
print(content)
file.close()


# 3️ Append Mode ('a')
# -> Adds new data at the end of the file
# -> Doesn’t delete previous content

file = open('example.txt', 'a')
file.write("This line is added using append mode.\n")
file.close()


# 4️ Read + Write Mode ('r+')
# -> Can both read and write
# -> Doesn’t overwrite entire file, starts writing from beginning

file = open('example.txt', 'r+')
print("Before writing (r+):")
print(file.read())
file.write("Writing from r+ mode.\n")
file.close()


# 5️ Write + Read Mode ('w+')
# -> Can read and write
# -> Deletes previous content and writes new

file = open('example.txt', 'w+')
file.write("This is w+ mode.\n")
file.seek(0)  # move cursor to start for reading
print("Reading after w+:")
print(file.read())
file.close()


# 6️ Append + Read Mode ('a+')
# -> Can read and append (adds new text at the end)
# -> Doesn’t delete old content

file = open('example.txt', 'a+')
file.write("Appending and reading using a+ mode.\n")
file.seek(0)
print("After a+ mode:")
print(file.read())
file.close()
