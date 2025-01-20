from prime import gcd


def solution033():
    prod_a = 1
    prod_b = 1

    for a in range(10, 100):
        for b in range(a + 1, 100):
            if a * b % 121 != 0:
                if (
                    b % 10 != 0
                    and a / b == (a // 10) / (b % 10)
                    and (a % 10) == b // 10
                ):
                    prod_a *= a // 10
                    prod_b *= b % 10

    return int(prod_b / gcd(prod_a, prod_b))
