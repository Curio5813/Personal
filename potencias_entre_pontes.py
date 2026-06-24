import math
import time


def potencias_entre_pontes():
    """
    Calcula a diferença entre dois fatores primos e as potências
    que resulta em números primos expurgados dos fatores compostos e
    achar as chaves privadas a partir de uma chave pública dada.
    """
    pass


def eh_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limite = math.isqrt(n)
    # Anda de 2 em 2 para testar apenas números ímpares
    for i in range(3, limite + 1, 2):
        if n % i == 0:
            return False
    return True


def executar_busca_primos():
    inicio = 300000
    fim = 400000

    tempo_inicial = time.perf_counter()
    total_primos = sum(1 for i in range(inicio, fim + 1) if eh_primo(i))
    tempo_final = time.perf_counter()

    tempo_gasto = (tempo_final - tempo_inicial) * 1000
    print(f"\n[Resultado] Total de primos encontrados: {total_primos}")
    print(f"Tempo de execução: {tempo_gasto:.2f} milissegundos\n")


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
    opcao = input("Escolha uma opção (1 ou 2): ")

    if opcao == "1":
        executar_busca_primos()
    elif opcao == "2":
        modulo_50_digitos = input("\nDigite a chave pública aqui: ")
        quadrados_perfeitos = encontrar_quadrados_subnumeros(modulo_50_digitos)

        print("\nLista de listas (ordenada por valor decrescente):")
        cont, modulacao, chave = 0, [], 0

        modulo_inteiro = int(modulo_50_digitos)
        tam_chave = len(modulo_50_digitos)

        for j in range(0, len(quadrados_perfeitos)):
            for k in range(0, 1):
                tentativa_primo = quadrados_perfeitos[j][3] * quadrados_perfeitos[j][1] * quadrados_perfeitos[j][2]
                rigor = len(str(tentativa_primo))

                # Ajuste na exponenciação para evitar floats (divisão inteira //)
                expoente = int((tam_chave // 2) - rigor)
                if expoente > 0:
                    modulacao.append(int(tentativa_primo * (10 ** expoente)))
                else:
                    modulacao.append(int(tentativa_primo))
            cont += 1
            if cont > 5:
                break

        cont = 0
        for j in range(0, len(modulacao)):
            base_inicial = modulacao[j]
            inicio_teste = max(2, base_inicial)

            # Otimização 1: Se o início for par, transforma em ímpar para o ciclo
            if inicio_teste % 2 == 0 and inicio_teste > 2:
                inicio_teste += 1

            # Otimização 2: Limitamos a busca a um raio realista (ex: 5 milhões de números)
            # Ir além disso em Python puro sem Crivo vai travar o processador
            limite_busca = 5000000

            # Otimização 3: O terceiro parâmetro (step=2) faz o loop saltar os pares
            passo = 1 if inicio_teste == 2 else 2
            for k in range(inicio_teste, inicio_teste + limite_busca, passo):
                if eh_primo(k):
                    if modulo_inteiro % k == 0:
                        chave = k
                        break

            if chave != 0:
                break

            cont += 1
            if cont > 5:
                break

        if chave != 0:
            print(f"Chave1: {chave} e Chave2: {modulo_inteiro // chave}")
        else:
            print(f"Chave1: {chave} e Chave2: Fatores não encontrados no raio de busca.")
