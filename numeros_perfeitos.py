def numeros_perfeitos():
    """
    Calcula todos os numeros perfeitos até 100.000
    :return:
    """
    divisores = []
    for i in range(1, 10000 + 1):
        for j in range(i - 1, 1 - 1, -1):
            if i % j == 0:
                divisores.append(j)
        if sum(divisores) == i:
            print(f"{i} é um numero perfeito")
        divisores = []


if __name__ == '__main__':
    numeros_perfeitos()