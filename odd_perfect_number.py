from math import pi


def odd_perfect_number():
    """
    This function return the decimal part of a odd perfect number.
    :return:
    """
    x = pi ** 17 / 6
    print(f"{x:.123f}")


odd_perfect_number()
