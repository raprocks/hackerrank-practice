inp =  int(input())

base_len = (2*inp)-1

'''
  *
 * *
* * * 
'''

for i in range(1,inp+1):

    out = " ".join(['*']*i).center(base_len, " ")
    print(out)
    
