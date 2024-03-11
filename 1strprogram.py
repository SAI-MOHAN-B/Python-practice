data_list = [12, 19, 14, 15, 14, 12, 15, 15]
min_occ = 1
temp = {}
element = None
for i in data_list:
    data = i
    if data in temp:
        temp[data] += 1
    else:
        temp[data] = 1

    if min_occ < temp[data]:
        min_occ = temp[data]
        element = data
if element is not None:
    print(element)
else:
    print("No element found")
