def solution017():
    uni = [
        "",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    ]

    dez = [
        "",
        "",
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    ]

    result = 0
    hsize = len("hundred")
    for i in range(1, 1000):
        result += len(uni[int(i // 100)])
        if i >= 100:
            result += hsize

        if i % 100 > 0:
            if i >= 100:
                result += len("and")
            if i % 100 < 20:
                result += len(uni[i % 100])
            else:
                result += len(dez[int((i % 100) // 10)]) + len(uni[(i % 100) % 10])

    result += len("one") + len("thousand")
    return result
