def solution076():
    to_sum = list(range(1, 100))
    value = 100

    result = [1]
    for i in range(value):
        result.append(0)

    for i in range(len(to_sum)):
        for j in range(to_sum[i], value + 1):
            result[j] += result[j - to_sum[i]]
    return result[-1]
