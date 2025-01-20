def get_cycle_length(d):
    zeros = 0
    zi = 2
    while str(1 / d)[zi] == 0:
        zeros += 1
    numerator = 10**zi
    digits = ""
    while True:
        current_digit = numerator // d
        if current_digit == 0 and numerator % d == 0:
            return 0  # no infinite cycle

        digits = f"{digits}{current_digit}"
        numerator = 10 * (numerator % d)

        if len(digits) > 10 and digits[-10:] in digits[:-10]:
            return len(digits) - digits[-10:].index(digits[-10:]) - 10


def solution026():
    max_d = None
    max_length = 0
    for d in range(7, 999):
        cycle_length = get_cycle_length(d)
        if cycle_length > max_length:
            max_d = d
            max_length = cycle_length

    return max_d
