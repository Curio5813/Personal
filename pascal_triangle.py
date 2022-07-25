from math import factorial


def newtonBinomial():
    """
    This fucntion create an of list the Newton's Binomial, until the
    values of numbers of terms given.
    """
    num = int(input("How many terms will have at the Newton's Binomial: "))
    print('')
    p_t, fat, cont, t = [], [], 0, num
    for i in range(num + 1):
        for k in range(num + 1):
            if t < 0:
                break
            binome = int(factorial(num) / (factorial(num - cont) * factorial(cont)))
            fat.append(binome)
            cont += 1
        p_t.append(fat)
        num -= 1
        fat = []
        cont = 0
        t -= 1
    p_t.reverse()
    return p_t


def pascalTriangle(p_t):
    """
    This function print the Pascal's Triangle.
    :param p_t:
    :return:
    """
    for i in range(0, len(p_t)):
        for k in range(0, len(p_t[i])):
            print(f"{(p_t[i][k]):>3}", end=' ')
        print('\n', end='')


pascalTriangle(newtonBinomial())