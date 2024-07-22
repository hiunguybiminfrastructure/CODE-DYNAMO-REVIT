items =IN[1]

result = []
for num in range(0,len(items),1):
    if num %2:
        result.append(items[num])

OUT =  result