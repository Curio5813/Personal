def math_olympiad_003():
    """
    Cubic equation.
    :return:
    """
    for x in range(1, 10):
        for y in range(1, 12):
            if x ** 3 - y ** 3 == 91:
                print(x, y)


math_olympiad_003()
