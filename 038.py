def is9pandigit(s):
    if len(s) != 9:
        return False
    digits = [0] * 9
    for digit in s:
        if digit == "0":
            return False
        if digits[int(digit) - 1] == 1:
            return False
        else:
            digits[int(digit) - 1] += 1
    return True


def solution038():
    max_pandigital = 0
    max_i = 0
    for i in range(1, 9999):
        s = ""
        n = 1
        while len(f"{s}{n * i}") <= 9:
            s = f"{s}{n * i}"
            n += 1
        if is9pandigit(s):
            if int(s) > max_pandigital:
                max_pandigital = int(s)

    return int(max_pandigital)
