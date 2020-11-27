test_cases = int(input())

for _ in range(test_cases):
    _ = input()
    set1 = set(map(int, input().split(" ")))
    _ = input()
    set2 = set(map(int, input().split(" ")))
    print(set1.issubset(set2))
