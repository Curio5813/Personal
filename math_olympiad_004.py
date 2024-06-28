from math import log


def math_olympiad_004():
    """
    Exponential problem.
    :return:
    """
    for i in range(-100, 100):
        for j in range(-100, 100):
            if j == 0:
                pass
            else:
                x = 2 ** (i / j) + 4 ** (i / j) + 8 ** (i / j)
                if log(x, 2) == log(155, 2):
                    print(i, j)


math_olympiad_004()
