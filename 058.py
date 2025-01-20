import math
import numba


@numba.jit(nopython=True)
def is_prime(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def solution058():
    curr = 3
    primes = 0
    non_primes = 1
    length = 3
    index = 1

    while True:
        if index % 4 == 0:
            non_primes += 1
            if primes / (primes + non_primes) < 0.1:
                return length
            length += 2
            index = 1
        else:
            index += 1
            if is_prime(curr):
                primes += 1
            else:
                non_primes += 1
        curr += length - 1
