def merge_the_tools(string, k):
    k = int(k)
    lst = []
    parts = len(string)//k
    count=0
    i=0
    while i<len(string):
        lst.append(string[count:count+k])
        count+=k
        i+=k
    for ele in lst:
        to_print = ""
        for char in ele:
            if char not in to_print:
                to_print += char
        print(to_print)
