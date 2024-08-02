names = ["Mark", "Markdown", "John", "Michael", "Ali"]
    #        0       1           2       3           4

#Mark-index Mark-0 

result = []
for num in range(len(names)):
    value = str(names[num]) + "-" + str(num)
    result.append(value)
print(result)