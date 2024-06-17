def equacao_cubica_02():
    """
    :return:
    """
    respostas = []
    for i in range(2, 1000 + 1):
        try:
            if (i ** 2 + ((16 * i ** 2) / (i - 4) ** 2)) == 180:
                respostas.append(i)
        except ZeroDivisionError:
            print("Divisão por zero! Passa!")
    if len(respostas) > 0:
        print(*respostas)
    else:
        print("A resposta não é um número inteiro!")


equacao_cubica_02()
