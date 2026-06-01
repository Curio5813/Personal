from math import sqrt


def potencias_entre_pontes():
    """
    Calcula a diferença entre dois fatores primos ou e as potências
    que resulta em numeros primos expurgados dos fatores compostos.
    O que chamo de potencias de pontes entre primos cofatores.
    :return:
    """
    lista = []
    num = int(input("Entre com um numero inteiro maior ou igual a 2: "))
    flag1 = 0
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0 and num != i:
            print('Não é primo', i)
            flag1 = 1
            break
    if not flag1:
        print('Primo')
    if flag1:
        for i in range(2, num + 1):
            j = i
            if sqrt(i) == int(sqrt(i)):
                i += 7
                if i % 2 == 0:
                    i += 1
                    lista.append(i)
                else:
                    lista.append(j)
            if (i - 7) > 7 and (i - 7) % 5 == 0:
                i -= 6
                if i % 2 == 0:
                    lista.append(i + 1)
                else:
                    lista.append(i)
            if i % 2 == 0:
                i += 1
                if i % 5 == 0 and i > 6:
                    i -= 6
                    if i % 2 == 0:
                        lista.append(i + 1)
                    else:
                        lista.append(i)
    if not flag1:
        for i in range(2, num + 1):
            j = i
            if sqrt(i) == int(sqrt(i)):
                i += 7
                if i % 2 == 0:
                    i += 1
                    lista.append(i)
                else:
                    lista.append(j)
            if (i - 7) > 7 and (i - 7) % 5 == 0:
                i -= 6
                if i % 2 == 0:
                    lista.append(i + 1)
                else:
                    lista.append(i)
            if i % 2 == 0:
                i += 1
                if i % 5 == 0 and i > 6:
                    i -= 6
                    if i % 2 == 0:
                        lista.append(i + 1)
                    else:
                        lista.append(i)
    a = sum(lista)
    g = max(lista)
    print(a, g)
    flag = 0
    if a % 5 == 0 or a % 7 == 0 or a % 11 == 0:
        print("Sim")
    for i in range(2, g):
        if g % i == 0 and g != i:
            print('Não é primo', i)
            flag = 1
            break
    if not flag:
        print('Primo')


potencias_entre_pontes()

