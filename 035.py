from prime import sieve


def get_rotations(n):
    result = []
    for i in range(len(str(n))):
        result.append(int(f"{str(n)[i:]}{str(n)[0:i]}"))
    return set(result) - {n}


def solution035():
    all_primes = sieve(1000000)
    primes = set()

    result = 1

    for prime in all_primes:
        if not set(["2", "4", "6", "8", "0"]).intersection(
            set([x for x in str(prime)])
        ):
            primes.add(prime)

    while primes:
        current_prime = primes.pop()
        all_permutations = get_rotations(current_prime)
        if not all_permutations:
            result += 1
        elif all([x in primes for x in all_permutations]):
            result += 1 + len(all_permutations)
            for p in all_permutations:
                primes.remove(p)
    return result
