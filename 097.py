def solution097():
    n = 1
    for i in range(783045):
        n *= 1024
        if n > 10**12:
            n = n % 10**11

    return ((n * 128) * 28433 + 1) % 10**10
