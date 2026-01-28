# tup = ("1", "2", "3", "4", "5")
# tup[0] = "10"

# print(tup[0])


# tup = (1,)

# print(type(tup) )


t = ( 1, 1 , 2 , 2 , 3 , 3 , 4 , 4  ,5 , 5 )
print(t)
new_tuple = set(t)
print("conert into set",new_tuple)
print(type(new_tuple))

alter_tuple = tuple(new_tuple)
print("conert into tuple again rewmove dublicate  \n ", alter_tuple)
print(type(alter_tuple))

