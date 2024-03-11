names_data = ['hello','guvi',23,'list']
print(len(names_data))
# adding the new content to the array
print(names_data+['GUVI'])
# printing the first two elements
print(names_data[:3])
names = input("Enter the names you wanted to search")
if names in names_data:
    print("data present in the names data")
else:
    print("given data Doesn't exists")

test_data = (12,13,14)
print(type(test_data))