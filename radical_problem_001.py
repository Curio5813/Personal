from math import sqrt


def radical_problem_001():
    """
    Radical problem.
    :return:
    """
    for x in range(1, 100):
        if sqrt(x + 2 * sqrt(x - 1)) == 3:
            print(x)


radical_problem_001()
