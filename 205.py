def make_dice_sums(sides, n_dice):
    dices = [1] * n_dice
    sums = {}

    while dices != [sides] * n_dice:
        if sum(dices) not in sums:
            sums[sum(dices)] = 1
        else:
            sums[sum(dices)] += 1

        i = -1
        dices[i] += 1
        while dices[i] > sides:
            dices[i] = 1
            i -= 1
            dices[i] += 1
    sums[sides * n_dice] = 1
    return sums


def solution205():
    pyramid_sums = make_dice_sums(4, 9)
    cubic_sums = make_dice_sums(6, 6)

    total = 0
    for pyramidal_sum in pyramid_sums:
        total += pyramid_sums[pyramidal_sum] * sum(
            [cubic_sums[x] for x in cubic_sums if x < pyramidal_sum]
        )
    return round(total / (4**9 * 6**6), 7)
