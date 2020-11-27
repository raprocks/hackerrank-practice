from collections import deque

num = int(input())
d = deque()
for _ in range(num):
    command = input()
    if len(command.split(" "))==2:
        command, argu = command.split(" ")

    if command=="append":
        d.append(argu)
    elif command=="pop":
        d.pop()
    elif command=="popleft":
        d.popleft()
    elif command=="appendleft":
        d.appendleft(argu)

for x in d:
    print(x, end=" ")
print()
