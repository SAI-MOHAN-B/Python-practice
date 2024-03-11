data_list = [12, 19, 14, 15, 14, 12, 15, 15]
min_occ = 1
temp = {}
res = []
element = None
for i in data_list:
    data = i
    if data in temp:
        temp[data] += 1
    else:
        temp[data] = 1
for names in temp:
    if temp[names] > 1:
        res.append(names)
print(res)
