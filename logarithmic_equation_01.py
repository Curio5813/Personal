from math import log


def logarithmic_equation_01():
    """
    Math Olympiad Germany
    :return:
    """
    for i in range(1, 10000):
        if 27 ** log(i, 3) + 3 ** log(i, 3) == 68:
            print(i)


logarithmic_equation_01()
