def is_pandigital(s):
    if "0" in s:
        return False
    result = [0] * 9
    for c in s:
        result[int(c) - 1] += 1
    if result == [1] * 9:
        return True
    else:
        return False


def solution032():
    result = set()
    for a in range(9, 99):
        for b in range(a + 1, 988):
            if is_pandigital(f"{a}{b}{a * b}"):
                result.add(a * b)

    for a in range(1, 10):
        for b in range(987, 9877):
            if is_pandigital(f"{a}{b}{a * b}"):
                result.add(a * b)

    return sum(result)
