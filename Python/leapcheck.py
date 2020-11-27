def is_leap(year):
    """TODO: Docstring for is_leap.

    :year: TODO
    :returns: TODO
The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
    """
    leap = False
    year = int(year)
    if year%4==0:
        if year%100==0:
            if year%400==0:
                leap = True
        elif year%100!=0:
            leap=True

    return leap
