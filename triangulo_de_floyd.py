from statistics import mean


def trianduloDeFloyd():
    """
    Esta função retorna um triângulo de Floyd, como segue abaixo:

    1
    2 3
    4 5 6
    7 8 9 10
    11 12 13 14 15
    16 17 18 19 20 21
    :return:
    """
    l, a, b, n = [], 1, 2, 2
    for i in range(0, 15):
        for k in range(a, b):
            print(f'{k:>3}', end=' ')
            l.append(k)
        a = b
        b = a + n
        n += 1
        print('\n', end='')
    print(mean(l))


trianduloDeFloyd()
