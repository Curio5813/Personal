import math


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
    opcao = input("Escolha uma opção (1 á 9): ")
    while opcao == 0:
        break
    else:
        if opcao in "123456789":
            modulo_50_digitos = input("\nDigite a chave pública aqui: ")
            quadrados_perfeitos = encontrar_quadrados_subnumeros(modulo_50_digitos)

            print("\nLista de listas (ordenada por valor decrescente):")
            modulacao, chave = [], 0

            modulo_inteiro = int(modulo_50_digitos)
            tam_chave = len(modulo_50_digitos)

            for j in range(0, len(quadrados_perfeitos)):
                for k in range(0, 1):
                    tentativa_primo = int(quadrados_perfeitos[j][3] * math.sqrt(quadrados_perfeitos[j][1]) * math.sqrt(quadrados_perfeitos[j][2]))
                    rigor = len(str(tentativa_primo))

                    # Ajuste na exponenciação para evitar floats (divisão inteira //)
                    expoente = int((tam_chave // 2) - rigor)
                    if expoente > 0:
                        modulacao.append(tentativa_primo * 10 ** expoente)
                    else:
                        modulacao.append(int(tentativa_primo))
            modulacao.sort()
            modulacao.reverse()
            # print(modulacao)
            for j in range(0, len(modulacao)):
                base_inicial = modulacao[j]
                inicio_teste = 2

                # Otimização 1: Se o início for par, transforma em ímpar para o ciclo
                if inicio_teste % 2 == 0 and inicio_teste > 2:
                    inicio_teste += 1

                # Otimização 2: Limitamos a busca a um raio realista (ex: 5 milhões de números)
                # Ir além disso em Python puro sem Crivo vai travar o processador
                limite_busca = len(modulo_50_digitos) // 2

                for k in range(inicio_teste, base_inicial * limite_busca):
                    # print(k)
                    if modulo_inteiro % k == 0:
                        chave = k
                        print(chave)
                        break

                if chave != 0:
                    break

            if chave != 0:
                print(f"Chave1: {chave} e Chave2: {modulo_inteiro // chave}")
            else:
                print(f"Chave1: {chave} e Chave2: Fatores não encontrados no raio de busca.")