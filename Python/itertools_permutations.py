from itertools import permutations

inp, r = input().strip().split()


for perm in sorted(permutations(inp, int(r))):
    print(''.join(perm))
