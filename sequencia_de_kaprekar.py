from copy import deepcopy


def sequencia_de_kaprekar():
    """
    A sequência de Kaprekar é um processo matemático curioso onde, a partir
    de qualquer número de 4 dígitos com pelo menos dois dígitos diferentes,
    você repete os seguintes passos:

    Ordena os dígitos em ordem crescente e decrescente.

    Subtrai o menor do maior.

    Repete o processo com o resultado.

    Esse processo sempre chega ao número 6174, conhecido como a constante de
    Kaprekar, em no máximo 7 passos. Depois disso, o número se repete indefinidamente:
    7641 - 1467 = 6174

    Essa constante foi descoberta pelo matemático indiano D. R. Kaprekar.
    :return:
    """
    while True:
        num1, num2, num_str1, num_str2, cont, passos = [], [], "", "", 0, 0
        numero = int(input("Digite um número inteiro de 4 dígitos com pelo menos dos "
                           "dígitos diferentes: "))
        if numero < 1000 or numero > 9999:
            while numero < 1000 or numero > 9999:
                numero = int(input("Digite um número inteiro de 4 dígitos: "))
        numero = str(numero)
        for i in range(0, len(numero)):
            num1.append(int(numero[i]))
        num1.sort()
        num2 = deepcopy(num1)
        num2.reverse()
        while True:
            for i in range(0, len(num1)):
                num_str1 += str(num1[i])
                num_str2 += str(num2[i])
            num_str1 = int(num_str1)
            num_srt2 = int(num_str2)
            diff = num_srt2 - num_str1
            passos += 1
            print(diff)
            if diff == 6174:
                print(f"A Constante de Kaprekar acontece depois de {passos} iterações!")
                break
            num1 = []
            numero2 = str(diff)
            for i in range(0, len(numero2)):
                num1.append(int(numero2[i]))
            num1.sort()
            num2 = deepcopy(num1)
            num2.reverse()
            num_str1 = ""
            num_str2 = ""


sequencia_de_kaprekar()
