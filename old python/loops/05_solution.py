# check which letter is less repeated
input_string = "mynameisayaz"

count = 1

for char in input_string:
    count +=1
    if input_string.count(char)==1:
        print(f"less repeacted {char} only repeated once ")
        
print(count)