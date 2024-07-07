from math import sqrt, e


def euler_number():
    """
    This function calculates the Euler number, a transcendental number
    used in calculating exponential equations and rate changes and which
    is itself its derivative. It's a divergente irracional number.
    :return:
    """
    n = float(input("How precisely you want the number: "))
    e_squared = (1 + (1 / sqrt(n))) ** sqrt(n)
    print(e_squared)
    print(e)


euler_number()
