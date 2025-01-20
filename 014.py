COLLATZ_CACHE = {1: 1}


def collatz_length(n):
    if n in COLLATZ_CACHE:
        return COLLATZ_CACHE[n]
    length = 1
    while n > 1:
        if n % 2 == 0:
            return 1 + collatz_length(int(n // 2))
        else:
            return 1 + collatz_length(3 * n + 1)

    return length


def solution014():
    longest = 0
    longest_chain = 0
    for i in range(1, 1000000 + 1):
        length = collatz_length(i)
        COLLATZ_CACHE[i] = length
        if length > longest_chain:
            longest = i
            longest_chain = length

    return longest
