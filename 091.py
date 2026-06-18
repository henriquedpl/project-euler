from numba import jit


@jit(nopython=True)
def is_rectangle(x0, y0, x1, y1):
    if (x0 * y1 - x1 * y0) != 0 and (
        (x0 * y0 + x1 * y1) == 0
        or ((x1 - x0) * x0 + (y1 - y0) * y0) == 0
        or ((x0 - x1) * x1 + (y0 - y1) * y1) == 0
    ):
        return True
    return False


def solution091():
    same_x = 0
    total = 0
    LIMIT = 50
    for x0 in range(0, LIMIT + 1):
        for y0 in range(0, LIMIT + 1):
            for x1 in range(0, x0 + 1):
                for y1 in range(0, LIMIT + 1):
                    if is_rectangle(x0, y0, x1, y1):
                        total += 1
                        if x0 == x1:
                            same_x += 1

    return int(total - int(same_x / 2))
