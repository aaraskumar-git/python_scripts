# Count characters in a string
str = 'araskumar'
count_dict = dict()
for ech in str:
    if ech not in count_dict.keys():
        count_dict[ech] = 1
    else:
        count_dict[ech] = count_dict[ech] + 1
print(count_dict)
