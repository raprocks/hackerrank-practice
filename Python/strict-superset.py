SetA = set(input().split(" "))
Sets = int(input())

for _ in range(Sets):
    test_set = set(input().split(" "))
    Switch = test_set.issubset(SetA)

    if Switch:
        diff = SetA.difference(test_set)
        if len(diff)==0:
            print(False)
            exit()
    else:
        print(False)
        exit()
print(True)
