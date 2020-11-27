n = int(input())
students = {}

for _ in range(n):
    inp = input().split(" ")
    students[inp[0]] = list(map(float, inp[1:]))

query = students[input()]

print(f"{sum(query)/len(query):.2f}")
