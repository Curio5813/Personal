def matrizInversa():
    """
    Esta função retorna a matriz inversa de uma dada matriz.
    :return:
    """
    print('='*60)
    print(f'{"ACHAR A MATRIZ INVERSA DE UMA MATRIZ QUADRADA":^60}')
    print('='*60)
    m, l1, l2 = [], [], []
    print('/n')
    x = int(input('Qual o tamanho da matriz? '))
    for i in range(x):
        for k in range(x):
            num = int(input(f'Qual o valor para linha {i} coluna {k} '))
            l1.append(num)
    print('/n')
    print('A matiz é:')
    print('/n')
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            print(l1[i][k])
    print('/n')
    for i in range(0, len(l1)):
        for k in range(0, len(l1)):
            l2.append(l1[i][k])


matrizInversa()
