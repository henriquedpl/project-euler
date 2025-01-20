from prime import prime_division


# We simply deduct 1/1000000, 1/999999, 1/999998 from the base fraction (3/7)
# until we find a fraction whose reduced form a/b has a,b < 1000000
def solution071():
    i = 1_000_000
    while i > 999995:
        num = 3 * i - 7
        den = 7 * i
        divs_num = dict(prime_division(num - 7))
        divs_den = dict(prime_division(den))
        for div in divs_num:
            if div in divs_den:
                num //= min([div ** divs_num[div], div ** divs_den[div]])
                den //= min([div ** divs_num[div], div ** divs_den[div]])
        if num <= 1_000_000 and den < 1_000_000:
            break
        i -= 1
    return num
