'''
Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
'''
inp = input()
diction = {}
for char in inp:
    if char in diction.keys():
        diction[char]+=1
    else:
        diction[char]=1
diction = diction.items()
sort1 = sorted(diction, key= lambda x: x[0])
sort1 = sorted(sort1, key= lambda x: x[1], reverse=True)
for x in range(3):
    print(sort1[x][0], sort1[x][1])
