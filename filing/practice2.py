# 1. Create and open file in write mode
file = open("intro.txt", "w")

# 2. Write some lines about yourself
file.write("My name is Ayaz.\nI love coding.\nPython is my favorite language.")
file.close()   # 3. Close the file

# 4. Reopen file in read mode
file = open("intro.txt", "r")

# 5. Read and print all contents
content = file.read()
print("File Content:\n", content)
file.close()

# 6. Count number of lines
file = open("intro.txt", "r")
lines = file.readlines()
print("Total Lines:", len(lines))
file.close()

# 7. Count number of words
file = open("intro.txt", "r")
words = file.read().split()
print("Total Words:", len(words))
file.close()

# 8. Count number of characters
file = open("intro.txt", "r")
characters = file.read()
print("Total Characters:", len(characters))
file.close()

# 9. Append one more line
file = open("intro.txt", "a")
file.write("\nI want to become a professional programmer.")
file.close()

# 10. Read file again and print final content
file = open("intro.txt", "r")
final = file.read()
print("\nFinal File Content:\n", final)
file.close()
