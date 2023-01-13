from math import hypot


def findHypotenuse():
    """
    this function returns the value of the hypotenuse knowing the
    values of the legs of a right triangle.
    :return:
    """
    a = float(input('Side A: '))
    b = float(input('Side B: '))
    c = hypot(a, b)
    print('')
    return print(f'Hypotenuse = {c:.2f}')


findHypotenuse()
