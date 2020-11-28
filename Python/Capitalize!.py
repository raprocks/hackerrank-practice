def solve(s):
    lst = s.split(" ")
    lst = list(map(lambda x : x.capitalize(), lst))
    return " ".join(lst)