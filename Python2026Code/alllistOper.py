# append

# ==============================
# 1. ADD ELEMENTS
# ==============================
# # lst = [1, 2, 3, "Ayaz"]
# lst.append(100)           # add at end
# lst.insert(1, 50)         # add at index
# lst.extend([200, 300])    # add multiple

# print(lst)



# ==============================
# 2. REMOVE ELEMENTS
# ==============================

# lst = [1, 2, 3, "Ayaz"]

# lst.remove(50)   # remove by value
# lst.pop()        # remove last
# lst.pop(0)       # remove by index

# print(lst)

# clear all
# temp = [1,2,3]
# temp.clear()
# # print(temp) 



# ==============================
# 3. ACCESS (INDEXING)
# ==============================

# lst = [10, 20, 30, 40]
# print(lst[0])     # first
# print(lst[-1])    # last


# ==============================
# 4. SLICING
# ==============================
# lst = [10,20,30,40,50,60,70,80,90,100]
# print(lst[1:3])   # [20, 30]
# print(lst[:2])    # [10, 20]
# print(lst[2:])    # [30, 40]

# ==============================
# 5. UPDATE (MUTABLE)
# ==============================

# lst[0] = 100
# print(lst)


x = 2
squares = [x**2 for x in range(5)]
print(squares)