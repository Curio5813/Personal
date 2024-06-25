from math import log


def logaritmos_001():
    """
    :return:
    """
    for i in range(1, 1000):
        if 27 ** log(i, 3) + 3 ** log(i, 3) == 68:
            return print(i)
    else:
        print("Não é inteiro!")


logaritmos_001()
