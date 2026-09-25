 
# read file 


# file = open('example.txt', 'r')
# content = file.read()    #read entire data
# print(content)
# file.close()


# Read first line  

# file = open('example.txt', 'r')
# content = file.readline() #read single line
# print(content)
# file.close() 


# Read first line  

# file = open('example.txt', 'r')
# content = file.readlines() #read entire data in list
# print(content)
# file.close() 


# write to a file 

# file = open('example2.txt', 'w') # this method rewrite the exisiting data with new data
# content = file.write('hello Bro! kasy ho.? ')
# print(content)
# file.close() 




# appened Mode - File_Handling

# file = open('example2.txt', 'a') # add data next to existing one do not overwrite the existing data
# content = file.write('\nAucha hun')
# print(content)
# file.close()


# close a file 
# using with statement 
with open ('example2.txt','r') as file:
    content = file.read()
    print(content)