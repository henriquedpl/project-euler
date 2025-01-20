import math
import functools
import operator
from prime import PrimeIterator


def expand_primes(primes, n, p):
    while primes[-1] < n:
        primes.append(next(p))
    return primes


def number_of_divisors(n, primes, p):
    i = 0
    divisors = {}

    while n > 1:
        if n % primes[i] == 0:
            n //= primes[i]
            if primes[i] not in divisors:
                divisors[primes[i]] = 1
            else:
                divisors[primes[i]] += 1
        else:
            i += 1
        if i == len(primes):
            expand_primes(primes, n, p)

    return functools.reduce(operator.mul, [divisors[x] + 1 for x in divisors])


def solution012():
    p = PrimeIterator()
    primes = [next(p) for i in range(100)]
    found = False
    i = 2
    while not found:
        _sum = (i * (i + 1)) / 2
        primes = expand_primes(primes, math.isqrt(int(_sum)) + 1, p)
        if _sum % 2 == 0 and number_of_divisors(_sum, primes, p) > 500:
            found = True
        else:
            i += 1

    return int(_sum)
