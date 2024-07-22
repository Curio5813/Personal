def dizima_periodica():
    """
    Esta função retorna a geratriz, a fração irredutivel, de uma dízima periódica dada.
    É importante frisar que para muitos caos de uma dízima temos os chamados números
    não computáveis.
    :return:
    """
    dizima = input("Digite uma dízima periódica com até 3 repetições do período: ")
    periodo, maior, cont, conjunto, idx, vezes, vezes1, flag = "", "", 0, [], 0, 0, 0, 0
    dizima = dizima[::-1]
    # achando a parte periódica da dízima
    for i in range(0, len(dizima)):
        periodo += dizima[i]
        if len(periodo) == periodo.count(dizima[i]) == 3:
            maior = periodo
            flag = 1
            break
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
        if deslocamento[1] == periodo:
            potencia10_1 = 1
            potencia10_2 = 10
            inteiro1 += "." + periodo
            inteiro1 = float(inteiro1)
            inteiro2 = inteiro1 * 10
            # parte inteira do calculo.
            inteiro1 = int(inteiro1)
            inteiro2 = int(inteiro2)
            print(inteiro1, inteiro2)
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
        if denominador < 1:
            print("O número é não computável.")
        else:
            print("A Geratriz é:")
            print(f"{numerador}/{denominador}", end=" ")
            # Busca por frações reduzidas
            for i in range(2, 10_000 + 1):
                if numerador % i == 0 and denominador % i == 0:
                    while numerador % i == 0 and denominador % i == 0:
                        numerador //= i
                        denominador //= i
                        cont += 1
    else:
        idx = len(maior)
        idx = idx
        periodo = maior
        periodo = periodo[::-1]
        dizima = dizima[::-1]
        inteiro1 = dizima.replace(".", "").split(periodo)
        inteiro1 = inteiro1[0]
        delocamento = dizima.split(".")
        if delocamento[1] == periodo:
            potencia10_1 = 1
            potencia10_2 = 10
            inteiro1 += "." + periodo
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
            inteiro1 = dizima.replace(".", "").split(periodo)
            inteiro1 = inteiro1[0]
            # Acha o tamanho da dízima
            potencia10_2_n = dizima.split(".")
            potencia10_2_n = potencia10_2_n[1].split(periodo)
            # Conta quantas casas decimais existem depois da parte inteira e antes da dízima
            potencia10_2_n = len(potencia10_2_n[0])
            # Acha o inteiro até a primeira repetição da dízima
            inteiro2 = dizima[0:-idx-1].replace(".", "")
            # As duas linha abaixo acha o denominador da fração subtraindo as potências de 10 para cada
            # parte inteira do calculo.
            potencia10_1 = 10 ** potencia10_2_n
            potencia10_2 = 10 ** (potencia10_2_n + idx + vezes)
            inteiro1 = int(inteiro1)
            inteiro2 = int(inteiro2)
            # Calcula o numerador
            numerador = inteiro2 - inteiro1
            # Calcula o denominador
            denominador = potencia10_2 - potencia10_1
            # printa a geratriz da dízima
            if denominador < 1:
                print("O número é não computável.")
            else:
                print("A Geratriz é:")
                print(f"{numerador}/{denominador}", end=" ")
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
