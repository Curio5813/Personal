def aposentadoria():
    """
    Problema 152 - FUNDAMENTOS DA MATEMÁTICA ELEMENTAR V. 11

    (Unesp-SP) Desejo ter, para minha aposentadoria, 1 milhão de reais. Para isso, faço uma
    aplicação financeira, que rende 1% de juros ao mês, já descontados o imposto de renda
    e as taxas bancárias recorrentes. Se desejo me aposentar após 30 anos com aplica-
    ções mensais fixas e ininterruptas nesse investimento, o valor aproximado, em reais,
    que devo disponibilizar mensalmente é:
    Dado: 1,01361 ≈ 36
    """
    for i in range(1, 500 + 1):
        prestacao = 0
        for j in range(0, 30 * 12):
            prestacao += i * (1 + 0.01) ** j
            if prestacao >= 1_000_000:
                return print(i)


aposentadoria()


