def print_formatted(number):
    n = number
    width = len(f"{n:b}")

    for i in range(1, int(n)+1):
        print(f"{i}".rjust(width) + " " + f"{i:o}".rjust(width) + " " + f"{i:X}".rjust(width) + " " + f"{i:b}".rjust(width))