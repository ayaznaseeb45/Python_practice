# File Handling Practice - Complete Program

# 1. Create a file named notes.txt and write 3 lines about yourself.
file = open("notes.txt", "w")
file.write("My name is Ayaz.\n")
file.write("I am learning Python.\n")
file.write("File handling is easy!\n")
file.close()

# 2. Read file content line by line.
file = open("notes.txt", "r")
for line in file:
    print(line.strip())
file.close()

# 3. Count total lines in the file.
file = open("notes.txt", "r")
line_count = 0
for line in file:
    line_count += 1
file.close()
print(f"\nTotal lines: {line_count}")

# 4. Append one more line to the file.
file = open("notes.txt", "a")
file.write("\nThis is an appended line.")
file.close()

# 5. Count how many words are in the file.
file = open("notes.txt", "r")
words = file.read().split()
# split krny word ko "list" meh lay ay ga
file.close()
print(f"Total words: {len(words)}")

# 6. Ask user to input a word and check if it exists in the file.
search = input("\nEnter a word to search: ")
file = open("notes.txt", "r")
data = file.read()
file.close()

if search in data:
    print(f"'{search}' found in file.")
else:
    print(f"'{search}' not found in file.")

# 7. Copy the content of notes.txt into a new file backup.txt.
source = open("notes.txt", "r")
target = open("backup.txt", "w")
target.write(source.read())
source.close()
target.close()

# 8. Replace a specific word in the file.
file = open("notes.txt", "r")
data = file.read()
file.close()

old = "Ayaz"
new = "Developer"
data = data.replace(old, new)

file = open("notes.txt", "w")
file.write(data)
file.close()
print(f"'{old}' replaced with '{new}'.")

# 9. Display all unique words from the file.
file = open("notes.txt", "r")
data = file.read().split()
file.close()

unique_words = set(data)
print("\nUnique words in the file:")
for word in unique_words:
    print(word)

# 10. Combine the contents of notes.txt and backup.txt into combined.txt.
file1 = open("notes.txt", "r")
file2 = open("backup.txt", "r")
combined = open("combined.txt", "w")

combined.write(file1.read() + "\n" + file2.read())
 
file1.close()
file2.close()
combined.close()
print("\nContents of both files combined into combined.txt.")
