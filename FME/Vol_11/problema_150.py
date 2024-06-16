def prestacoes_01():
    """
    (FGV-SP) Ao investir todo mês o montante de R$ 1 200,00 em uma aplicação financeira,
    o investidor notou que imediatamente após o terceiro depósito, seu montante total era de
    R$ 3 900,00. A taxa mensal de juros dessa aplicação, em regime de juros compostos, é:
    :return:
    """
    montante, prestacao, valor = 3900, 1200, 0
    for i in range(0, 3 + 1):
        valor += prestacao * (1 + ((10 ** (1 / 2) - 3) / 2) / 100) ** i
        print(valor)
        if valor >= montante:
            print(valor)
            break


prestacoes_01()


