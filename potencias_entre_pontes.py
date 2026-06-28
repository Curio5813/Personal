import math
from statistics import median
from time import time


tempo_inicial = time()

def potencias_entre_pontes():
    """
    Calcula a diferença entre dois fatores primos e as potências
    que resulta em números primos expurgados dos fatores compostos e
    achar as chaves privadas a partir de uma chave pública dada.
    """


def encontrar_quadrados_subnumeros(numero_str):
    n = len(numero_str)
    resultados = []

    for tamanho in range(1, n + 1):
        for inicio in range(n - tamanho + 1):
            sub_str = numero_str[inicio: inicio + tamanho]
            if not sub_str:
                continue

            valor = int(sub_str)

            if valor == 0:
                resultados.append([valor, inicio + 1, inicio + tamanho, 0])
            else:
                raiz = int(math.isqrt(valor))
                if raiz * raiz == valor:
                    resultados.append([valor, inicio + 1, inicio + tamanho, raiz])

    resultados.sort(key=lambda x: x[0], reverse=True)
    return resultados


if __name__ == "__main__":
    print("=== MENU DE TESTES ===")
    print("1 - Contar primos no intervalo (300k a 400k)")
    print("2 - Procurar quadrados perfeitos na chave de 50 dígitos")
    opcao = input("\nEscolha uma opção (1 á 9): ")
    while opcao == 0:
        break
    else:
        if opcao in "123456789":
            # 100000000000031 100000000001087
            chaves_privadas = list(map(int, input("\nDigite os dois primos: ").split()))
            modulo_50_digitos = str(chaves_privadas[0] * chaves_privadas[1])
            print(f"A Chave Pública é {modulo_50_digitos}")
            quadrados_perfeitos = encontrar_quadrados_subnumeros(modulo_50_digitos)

            print("\nValores mais próximos do alvo:")
            modulacao, chave = [], 0

            modulo_inteiro = int(modulo_50_digitos)
            tam_chave = len(modulo_50_digitos)
            expoente = int((math.ceil(tam_chave / 2)))

            rigor = 0
            for j in range(0, len(quadrados_perfeitos)):

                for k in range(0, 1):
                    tentativa_primo = int((quadrados_perfeitos[j][3] * math.sqrt(quadrados_perfeitos[j][1]) *
                                       math.sqrt(quadrados_perfeitos[j][2])))
                    print(tentativa_primo)
                    rigor = len(str(tentativa_primo))
                    if tentativa_primo == 0:
                        break
                    else:
                        modulacao.append(tentativa_primo ** (rigor))
            modulacao.sort()
            print(modulacao)
            minimo = min(modulacao)
            mediana = int(median(modulacao))
            maximo = max(modulacao)
            print(minimo, mediana, maximo)
            print(sum(modulacao) ** 2   )

            flag = False

            for j in range(3, 100_000 + 1, 2):
                if modulo_inteiro % j == 0:
                    chave = j
                    flag = True
                    break
            if not flag:
                for j in range(minimo + 1, minimo * 10, 2):
                    if modulo_inteiro % j == 0:
                        chave = j
                        flag = True
                        break
            if not flag:
                for j in range(maximo + 1, maximo // 10, -2):
                    if modulo_inteiro % j == 0:
                        chave = j
                        flag = True
                        break
            if not flag:
                for j in range(mediana + 1, int(minimo * (5/4)), 2):
                    if modulo_inteiro % j == 0:
                        chave = j
                        flag = True
                        break
            if not flag:
                for j in range(mediana + 1, int(minimo * (5/4)), -2):
                    if modulo_inteiro % j == 0:
                        chave = j
                        flag = True
                        break

            print(f"Chave1: {chave} e Chave2: {modulo_inteiro // chave}.")

tempo_final = time()

tempo_total = tempo_final - tempo_inicial
print(tempo_total)


# 321698972922577370385350057131
# 383147160123599
# 839622490791269