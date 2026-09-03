# a = 10
# b = 10.5
# c = "20"
# d = [1, 2, 3]
# e = (4, 5, 6)
# f = {7, 8, 9}
# g = {"name": "Ayaz"}
# h = True

# # Part A:
# print(type(a), type(b), type(c), type(d), type(e), type(f), type(g), type(h))

# # Part B:
# x = int(c) + a
# y = str(a) + c
# z = list(e)

# print(x, y, z)

# # Part C:
# d[0] = 100
# # e[0] = 100   (will it work?)

# print(d, e)


# a = "50"
# b = 20
# print(a + str(b))

# x = "10.5"
# print(int(float(x)))


# x = "100"
# y = 50
# print(int(x) + y)


# a = "10"
# b = 5

# x = int(a) + b
# y = a + str(b)


# print(x, type(x))
# print(y , type (y))


# x = "10.5"
# print(int(float(x)))


# a = 0
# b = 5
# print(bool(a), bool(b))


# a = [1,2,3]
# b = tuple(a)
# print(b)


# a = 2 + 3j
# b = 1 + 2j

# c = a + b
# d = a * b

# print(c)
# print(d)


# x = 20
# print(str(x))     # "20"

# lst = ['a','b','c']
# name1 = "Ayaz"
# name2 = "Khan"



# print("-".join([name1,name2]))



# ============= string operations =============
# ==============================
# PYTHON STRING OPERATIONS NOTES
# ==============================


# # 📌 1. Concatenation (+)
# # Use: 2 strings ko jorna (combine)

# first = "Hello"
# second = "Ayaz"
# print(first + " " + second)   # Hello Ayaz


# # 📌 2. Indexing
# # Use: specific character nikalna

# s = "Python"
# print(s[0])   # P
# print(s[3])   # h


# # 📌 3. Slicing
# # Use: string ka part nikalna

# print(s[0:3])   # Pyt
# print(s[2:])    # thon


# # 📌 4. Length (len)
# # Use: string ki length check karna

# print(len("Ayaz"))   # 4


# # 📌 5. Check (in)
# # Use: check karna word exist karta hai ya nahi

# print("Py" in s)     # True
# print("Java" in s)   # False


# # 📌 6. Replace
# # Use: word change karna

# s = "Hello Ayaz"
# print(s.replace("Ayaz", "Ali"))   # Hello Ali


# # 📌 7. Case Conversion
# # Use: text ka format change karna

# s = "python"
# print(s.upper())   # PYTHON
# print(s.lower())   # python


# # 📌 8. Strip
# # Use: extra spaces remove karna

# s = "  hello  "
# print(s.strip())   # "hello"


# # 📌 9. Split
# # Use: string ko list me todna

# s = "a,b,c"
# print(s.split(","))   # ['a', 'b', 'c']


# # 📌 10. Join
# # Use: list ko string banana

# lst = ['a', 'b', 'c']
# print("-".join(lst))   # a-b-c


# # 📌 11. Find
# # Use: position find karna

# s = "Python"
# print(s.find("t"))   # 2


# ==============================
# FINAL SUMMARY
# ==============================

# Concatenate → jorna
# Index → ek character lena
# Slice → part lena
# len → length
# in → check
# replace → change
# upper/lower → format
# strip → space remove
# split → todna
# join → jorna
# find → position


# ============= string operations =============

list1 = [1, 2, 3]

print(list1.append(4))   
print(list1)             