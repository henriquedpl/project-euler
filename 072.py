def solution072():
    limit = 1_000_000
    phi = list(range(limit + 1))
    for p in range(2, limit + 1):
        if phi[p] == p:  # p is prime
            for k in range(p, limit + 1, p):
                phi[k] *= p - 1
                phi[k] //= p

    result = sum(phi[1:])
    return result
