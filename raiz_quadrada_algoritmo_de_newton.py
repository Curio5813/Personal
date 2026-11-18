def raiz_quadrada_algoritmo_de_newton():
    """
    Algoritmo de Newton para extração da raiz quadrada de um numero inteiro.
    :return:
    """
    num = int(input())
    raiz = 0
    if num < 0:
        print('Numero negativo. Não existem raízes reais.')
    elif num == 0:
        print(num)
    elif num == 1:
        print(num)
    else:
        a = num - 1
        for i in range(20):
            raiz = (1 / 2) * (a + num / a)
            a = raiz
        print(raiz)


raiz_quadrada_algoritmo_de_newton()
