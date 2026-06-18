from prime import prime_division

divisors = {}
for i in range(2, 50 + 1):
    divisors[i] = prime_division(i)


def perm(c, g):
    numerator_divisors = {}
    denominator_divisors = {}
    numerator = [x for x in range(min(c, g) + 1, c + g + 1)]
    denominator = [x for x in range(2, (max(c, g)) + 1)]
    for n in numerator:
        for p in divisors[n]:
            if p[0] not in numerator_divisors:
                numerator_divisors[p[0]] = p[1]
            else:
                numerator_divisors[p[0]] += p[1]

    for d in denominator:
        for p in divisors[d]:
            if p[0] not in denominator_divisors:
                denominator_divisors[p[0]] = p[1]
            else:
                denominator_divisors[p[0]] += p[1]

    for n in numerator_divisors:
        if n in denominator_divisors:
            numerator_divisors[n] = numerator_divisors[n] - denominator_divisors[n]

    result = 1
    for n in numerator_divisors:
        result *= n ** numerator_divisors[n]
    return result


def solution116():
    result = 1
    for red_tiles in range(1, int(50 / 2)):
        grey_tiles = 50 - red_tiles * 2
        print(f"Red tiles: {red_tiles} Grey tiles: {50 - 2*red_tiles}")
        result += perm(red_tiles, grey_tiles)

    for green_tiles in range(1, int(50 / 3) + 1):
        grey_tiles = 50 - green_tiles * 3
        print(f"Green tiles: {green_tiles} Grey tiles: {50 - 3*green_tiles}")
        result += perm(green_tiles, grey_tiles)

    for blue_tiles in range(1, int(50 / 4) + 1):
        grey_tiles = 50 - blue_tiles * 4
        print(f"Blue tiles: {blue_tiles} Grey tiles: {50 - 4*blue_tiles}")

        result += perm(blue_tiles, grey_tiles)

    return result
