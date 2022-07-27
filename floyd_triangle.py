def trianguloDeFloyd():
    """
    This function return the Floyd Triangle as showed below.

    1
    2 3
    4 5 6
    7 8 9 10
    11 12 13 14 15
    16 17 18 19 20 21
    :return:
    """
    l, a, b, n = [], 1, 2, 2
    rows = int(input(f'Number of rows: '))
    for i in range(0, rows):
        for k in range(a, b):
            print(f'{k:>2}', end=' ')
        a = b
        b = a + n
        n += 1
        print('\n', end='')


trianguloDeFloyd()
