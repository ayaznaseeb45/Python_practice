import csv

# # write data
# with open('example.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['ayaz','45', 'khuiratta'])

# # read file r 
# with open('example.csv', 'r') as file:
#     reader = csv.reader(file)
#     print("reading csv content")
#     for row in reader:
#         print(row)

with open ('example.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Laiba", 21, "Lahore"])
print("Data appended to CSV.")


