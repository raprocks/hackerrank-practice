n, modulo = map(int, input().strip().split())

lists = []

for _ in range(n):
    lists.append(list(map(int, input().strip().split()))[1:])
sum_squared = 0
for each in lists:
    maximum = max(each)
    sum_squared += maximum**2
print(sum_squared % modulo)
