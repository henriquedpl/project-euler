import math
import functools
import operator


class PrimeIterator:
    def __init__(self):
        self.primes = []
        self.n = 2

    def __next__(self):
        if not self.primes:
            self.primes.append(self.n)
            self.n = 3
            return self.primes[-1]
        else:
            i = 0
            while self.primes[i] <= math.isqrt(self.n):
                if self.n % self.primes[i] == 0:
                    i = 0
                    self.n += 2
                else:
                    i += 1
            self.primes.append(self.n)
            self.n += 2
            return self.primes[-1]


def sieve(max_prime):
    sieve = [True] * max_prime
    sieve[0] = False

    for n in range(2, max_prime // 2 + 1):
        if sieve[n - 1]:
            m = 2
            while (n * m) <= len(sieve):
                sieve[m * n - 1] = False
                m += 1
    return [i + 1 for i in range(len(sieve)) if sieve[i]]


def prime_division(n):
    p = PrimeIterator()
    result = []
    while n != 1:
        current_prime = next(p)
        if n % current_prime == 0:
            n = n // current_prime
            result.append((current_prime, 1))
            while n % current_prime == 0:
                n = n // current_prime
                result[-1] = (current_prime, result[-1][1] + 1)
    return result


def is_prime(n):
    for i in range(3, math.floor(math.isqrt(n))):
        if n % i == 0:
            return False
    return True


def gcd(a, b):
    divs_a = dict(prime_division(a))
    divs_b = dict(prime_division(b))

    gcd = {}
    for divisor in divs_a:
        if divisor in divs_b:
            gcd[divisor] = min([divs_a[divisor], divs_b[divisor]])
    return functools.reduce(operator.mul, [x ** gcd[x] for x in gcd])
