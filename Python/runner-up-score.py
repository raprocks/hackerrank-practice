n = int(input())
arr = map(int, input().split(" "))
arr = set(arr)
arr = list(arr)
arr.sort(reverse=True)
print(arr[1])

