from prime import sieve
import math


def solution087():
    limit = 50_000_000
    square_limit = int(math.sqrt(limit))
    cube_limit = int(limit ** (1 / 3))
    fourth_limit = int(math.sqrt(square_limit))

    square_primes = sieve(square_limit + 1)
    cube_primes = [x for x in square_primes if x <= cube_limit + 1]
    fourth_primes = [x for x in square_primes if x <= fourth_limit + 1]

    sum_set = set()
    for s in square_primes:
        for c in cube_primes:
            for f in fourth_primes:
                n = s**2 + c**3 + f**4
                if n < limit:
                    sum_set.add(n)

    return len(sum_set)
