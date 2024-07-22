def dizima_periodica():
    """
    Esta função retorna a geratriz, a fração irredutivel, de uma dízima periódica dada.
    É importante frisar que para muitos casos de uma dízima temos os chamados números
    não computáveis. De fato, há bem mais números não-computáveis que computávies.
    :return:
    """
    dizima = input("Digite uma dízima periódica: ")
    periodo, maior, cont, conjunto, idx, vezes, vezes1, flag = "", "", 0, [], 0, 0, 0, 0
    dizima = dizima[::-1]
    # achando a parte periódica da dízima
    for i in range(0, len(dizima)):
        periodo += dizima[i]
        if len(periodo) == periodo.count(dizima[i]) == 3:
            maior = periodo
            flag = 1
        if len(periodo) >= 2 and dizima.count(periodo) >= 2:
            vezes += 1
            maior = periodo
            for j in maior:
                conjunto.append(j)
        else:
            vezes1 += 1
    if flag == 1:
        periodo = maior
        periodo = periodo[::-1]
        dizima = dizima[::-1]
        ponto1 = dizima.split(".")
        ponto1 = ponto1[0]
        diff = len(ponto1)
        inteiro1 = dizima.replace(".", "").split(periodo)
        inteiro1 = inteiro1[0]
        idx1 = len(inteiro1)
        idx2 = len(inteiro1) + 1
        deslocamento = dizima.split(".")
        deslocamento[1] = periodo
        tentar = dizima.split(".")
        verificacao = tentar[1]
        if deslocamento[1] == periodo and deslocamento[1] == verificacao:
            potencia10_1 = 1
            potencia10_2 = 10
            inteiro1 = deslocamento[0] + "." + periodo
            inteiro1 = float(inteiro1)
            inteiro2 = inteiro1 * 10
            # parte inteira do calculo.
            inteiro1 = int(inteiro1)
            inteiro2 = int(inteiro2)
            # Calcula o numerador
            numerador = inteiro2 - inteiro1
            # Calcula o denominador
            denominador = potencia10_2 - potencia10_1
        else:
            inteiro1 += "." + periodo
            inteiro1 = float(inteiro1)
            inteiro2 = inteiro1 * 10
            # parte inteira do calculo.
            inteiro1 = int(inteiro1)
            inteiro2 = int(inteiro2)
            # Calcula o numerador
            numerador = inteiro2 - inteiro1
            # Calcula o denominador
            potencia10_1 = 10 ** (idx1 - diff)
            potencia10_2 = 10 ** (idx2 - diff)
            denominador = potencia10_2 - potencia10_1
            # printa a geratriz da dízima
            print("A Geratriz é:")
            print(f"{numerador}/{denominador}", end=" ")
            if denominador < 1:
                print("Dízima não computável!")
                return 0
            # Busca por frações reduzidas
        for i in range(2, 10_000 + 1):
            if numerador % i == 0 and denominador % i == 0:
                while numerador % i == 0 and denominador % i == 0:
                    numerador //= i
                    denominador //= i
                    cont += 1
    else:
        idx = len(maior)
        periodo = maior
        periodo = periodo[::-1]
        dizima = dizima[::-1]
        inteiro1 = dizima.replace(".", "").split(periodo)
        inteiro1 = inteiro1[0]
        delocamento = dizima.split(".")
        delocamento[1] = periodo
        tentar = dizima.split(".")
        verificacao = tentar[1][0:idx]
        if delocamento[1] == verificacao:
            diff_dizima = dizima.split(".")
            diff_dizima = diff_dizima[0]
            diff = len(inteiro1) - len(diff_dizima)
            potencia10_1 = 10 ** diff
            inteiro2 = inteiro1 + periodo
            potencia10_2 = 10 ** (len(inteiro2) - len(inteiro1))
            inteiro1 = int(inteiro1)
            inteiro2 = int(inteiro2)
            # Calcula o numerador
            numerador = inteiro2 - inteiro1
            # Calcula o denominador
            denominador = potencia10_2 - potencia10_1
            # printa a geratriz da dízima
            print("A Geratriz é:")
            print(f"{numerador}/{denominador}", end=" ")
            if denominador < 1:
                print("Dízima não computável!")
                return 0
            # Busca por frações reduzidas
            for i in range(2, 10_000 + 1):
                if numerador % i == 0 and denominador % i == 0:
                    while numerador % i == 0 and denominador % i == 0:
                        numerador //= i
                        denominador //= i
                        cont += 1
            if denominador == 1:
                print("ou", end=" ")
                print(f"{numerador}")
            else:
                if cont > 0:
                    print("ou", end=" ")
                    print(f"{numerador}/{denominador}")
        else:
            diff_dizima = dizima.split(".")
            diff_dizima = diff_dizima[0]
            diff = len(inteiro1) - len(diff_dizima)
            potencia10_1 = 10 ** diff
            inteiro2 = inteiro1 + periodo
            potencia10_2 = 10 ** (diff + len(periodo))
            inteiro1 = int(inteiro1)
            inteiro2 = int(inteiro2)
            # Calcula o numerador
            numerador = inteiro2 - inteiro1
            # Calcula o denominador
            denominador = potencia10_2 - potencia10_1
            # printa a geratriz da dízima
            print("A Geratriz é:")
            print(f"{numerador}/{denominador}", end=" ")
            if denominador < 1:
                print("Dízima não computável!")
                return 0
            # Busca por frações reduzidas
            for i in range(2, 10_000 + 1):
                if numerador % i == 0 and denominador % i == 0:
                    while numerador % i == 0 and denominador % i == 0:
                        numerador //= i
                        denominador //= i
                        cont += 1
            if denominador == 1:
                print("ou", end=" ")
                print(f"{numerador}")
            else:
                if cont > 0:
                    print("ou", end=" ")
                    print(f"{numerador}/{denominador}")


dizima_periodica()
