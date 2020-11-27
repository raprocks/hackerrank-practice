_ = input().strip()

A = set(map(int, input().strip().split()))

operations = int(input().strip())

for _ in range(operations):
    command, _ = input().strip().split()
    B = set(map(int, input().strip().split()))
    if command == "intersection_update":
        A.intersection_update(B)
    elif command == "update":
        A.update(B)
    elif command == "symmetric_difference_update":
        A.symmetric_difference_update(B)
    elif command == "difference_update":
        A.difference_update(B)

print(sum(A))
