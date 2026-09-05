list1 = [1,2,3,5]

n = len(list1)  
# print(n) //4

for i in range(1, n + 1):
    # print (i)
    if i not in list1:
        print("Missing number is:", i)

