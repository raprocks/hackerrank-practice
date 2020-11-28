s = input()

lst = list(s)

alpha = False
digit = False
lower = False
upper = False

for each in lst:
    if not alpha:
        alpha = each.isalpha()
    if not digit:
        digit = each.isdigit()
    if not lower:
        lower = each.islower()
    if not upper:
        upper = each.isupper()
alphanum = alpha or digit
print(alphanum)
print(alpha)
print(digit)
print(lower)
print(upper)
