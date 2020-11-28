N,M = map(int, input().strip().split())
"|.-WELCOME"
mid = int(N/2)
mid_label = "WELCOME".center(M, '-')

for i in range(1, mid+1):
    print(((".|."*((2*i)-1)).center(M,'-')))
print(mid_label)
for i in range(mid, 0, -1):
    print(((".|."*((2*i)-1)).center(M,'-')))