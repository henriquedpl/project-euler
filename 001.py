def solution001():
    div_3 = int(999 / 3)
    div_5 = int(999 / 5)
    div_15 = int(999 / 15)

    return (
        3 * (div_3) * (div_3 + 1)
        + 5 * (div_5) * (div_5 + 1)
        - 15 * (div_15) * (div_15 + 1)
    ) / 2
