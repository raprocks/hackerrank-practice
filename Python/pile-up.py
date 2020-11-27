from collections import deque


testcase = input()

for _ in range(int(testcase)):
    d = deque()
    boxes = int(input())
    box_len = input()
    for length in box_len.split(" "):
        d.append(int(length))

    stack = []
    if d[0] >= d[-1]:
        stack.append(d[0])
        d.popleft()
    elif d[-1] >= d[0]:
        stack.append(d[-1])
        d.pop()

    for _ in range(boxes-1):
        big,where = (d[0],"left") if d[0]>=d[-1] else (d[-1],"right")
        stack.append(int(big))
        if where=="left":
            d.popleft()
        else:
            d.pop()

    stack_copy = stack.copy()
    stack.sort(reverse=True)
    if stack==stack_copy:
        print("Yes")
    else:
        print("No")
