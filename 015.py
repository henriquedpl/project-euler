import functools
import operator


# simple permutation with repetition
# to go from corner to corner it requires 20 moves right and 20 moves
# down, with can be permutated with 20 repetitions for each
# = 40!/(20! * 20!)
# = (40 * 39 * 38 * ... * 21) / 20!
# this could be further reduced using divisions in both sides
def solution015():
    numerator = functools.reduce(operator.mul, list(range(21, 41)))
    denominator = functools.reduce(operator.mul, list(range(1, 21)))

    return int(numerator / denominator)
