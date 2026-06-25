import math


def is_pandigital(n):
    if type(n) == int and n < 10**9:
        return False
    if "0" in str(n)[-9:]:
        return False
    if len(set(c for c in str(n)[-9:])) == 9:
        return True
    return False


def solution104():
    SQRT5 = math.sqrt(5)

    i = 2
    n_1 = 1
    n_2 = 1

    n_neg_preffix = (-1 / SQRT5) * (0.5 - SQRT5 / 2) ** 2
    n_pos_preffix = (1 / SQRT5) * (0.5 + SQRT5 / 2) ** 2

    while True:
        i += 1
        n_next_suffix = n_1 + n_2
        n_neg_preffix *= 0.5 - SQRT5 / 2
        n_pos_preffix *= 0.5 + SQRT5 / 2
        if n_next_suffix > 10**12:
            n_next_suffix = n_next_suffix % (10**12)
        if n_neg_preffix > 10**24:
            n_neg_preffix /= 10**24
        if n_pos_preffix > 10**24:
            n_pos_preffix /= 10**24
        if is_pandigital(n_next_suffix):
            if is_pandigital(
                str(float(n_neg_preffix + n_pos_preffix)).replace(".", "")[:9]
            ):
                return i
        n_1 = n_2
        n_2 = n_next_suffix


print(solution104())
