from math import factorial


def mega_sena_probability():
    """
    This function calculate the probability to win the MegaSena prize
    in a simple game.
    :return:
    """
    comb = factorial(60) / (factorial(6) * (factorial(60 - 6)))
    return print(f"{1/comb}%")


mega_sena_probability()
