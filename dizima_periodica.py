from collections import defaultdict


def dizima_periodica():
    """
    This functions gives the irreductible fraction
    from a periodic dizima, called geratriz.
    :return:
    """
    dizima = input("Digite uma dízima periódica com até duas repetições da parte periódica: ")
    n = len(dizima)
    substring_cont = defaultdict(int)
    cont = 0
    # Gera todas as substrings
    for i in range(1, n + 1):  # Tamanho da substring
        for j in range(n - i + 1):  # Indice da substring
            substring = dizima[j:j + i]
            substring_cont[substring] += 1
    maior_substring = ''
    maior_frequencia = 0
    for substring, count in substring_cont.items():
        if count > 1:
            if len(substring) > len(maior_substring) or (
                    len(substring) == len(maior_substring) and count > maior_frequencia):
                maior_substring = substring
    inteiro1 = dizima.replace(".", "").split(maior_substring)
    inteiro1 = inteiro1[0]
    # Acha o tamanho da dízima
    idx = len(maior_substring)
    potencia10_2_n = dizima.split(".")
    potencia10_2_n = potencia10_2_n[1].split(maior_substring)
    # Conta quantas casas decimais existem depois da parte inteira e antes da dízima
    potencia10_2_n = len(potencia10_2_n[0])
    # Acha o inteiro até a primeira repetição da dízima
    inteiro2 = dizima[0:-idx].replace(".", "")
    # As duas linha abaixo acha o denominador da fração subtraindo as potências de 10 para cada
    # parte inteira do calculo.
    potencia10_1 = 10 ** potencia10_2_n
    potencia10_2 = 10 ** (potencia10_2_n + idx)
    inteiro1 = int(inteiro1)
    inteiro2 = int(inteiro2)
    # Calcula o numerador
    numerador = inteiro2 - inteiro1
    # Calcula o denominador
    denominador = potencia10_2 - potencia10_1
    # printa a geratriz da dízima
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
