import itertools

n, modulo = map(int, input().strip().split())


def itersum(x):
    total = sum(i**2 for i in x)
    return total


lists = []

for _ in range(n):
    lists.append(list(map(int, input().strip().split()))[1:])

iters = itertools.product(*lists)

totals = [itersum(x)%modulo for x in iters]
print(max(totals))
