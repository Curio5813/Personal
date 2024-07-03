from math import sqrt


def math_olympiad_005():
    """
    Radical Problem.
    :return:
    """
    flag = 0
    for a in range(1, 100 + 1):
        for b in range(1, 100 + 1):
            if sqrt(a) + sqrt(b) == 10 and sqrt(a * b) == 10:
                flag = 1
                print(a, b)
    if flag == 0:
        print("It's not integer!")


math_olympiad_005()
