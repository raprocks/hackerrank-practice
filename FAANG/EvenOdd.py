dict = {
        1:'one',
        2:'two',
        3:'three',
        4:'four',
        5:'five',
        6:'six',
        7:'seven',
        8:'eight',
        9:'nine'
        }
# A dictionary with keys as integers and values as their English equivalent spelled out

a = int(input()) # take start integer
b = int(input()) # take end integer

for x in range(a, b+1):
    #make a for statement with x ranging from 'a' to 'b+1' as range gives output from first parameter to second parameter but not including the second parameter. So we simply increase the second parameter by 1.
    if x in dict.keys(): # if x in dictionary keys
        print(dict[x]) # print value of integer as English equivalent
    elif x%2 == 0: # else if even
        print("even") # print even
    elif x%2 != 0: # else if odd
        print("odd") # print odd

