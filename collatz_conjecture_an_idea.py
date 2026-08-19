import math


def collatz_conjecture_an_idea():
    print("Buscando números triangulares válidos...")
    print("Critérios: Qualquer dígito ímpar | Sem dígitos 2 e 3 | Passa por 2^32")
    print("-" * 60)

    encontrados = 0
    # Limite mínimo: 2^32 (4.294.967.296)
    limite_potencia = 16

    # Varre geradores n para calcular os números triangulares diretamente
    for n in range(1, 5_000):
        # Fórmula exata do número triangular
        triangular = (n * (n + 1)) // 2

        # 1. Filtro: Deve ser um número ÍMPAR
        if triangular % 2 == 0:
            continue

        # 2. Filtro de dígitos: Não pode conter os algarismos '2' ou '3'
        texto_num = str(triangular)
        if '2' in texto_num or '3' in texto_num:
            continue

        # 3. Teste da Conjectura de Collatz
        copia = triangular
        passou_pela_potencia = False

        # Simula a órbita de Collatz por até 500 passos
        for _ in range(500):
            # Se o número atingir uma potência pura de 2 maior ou igual a 2^32...
            if copia >= limite_potencia and (copia & (copia - 1)) == 0:
                # Descobrimos o expoente da potência usando logaritmo binário
                expoente = int(math.log2(copia))
                # Se ele entrar direto em 2^32, ou em uma potência maior (par ou ímpar),
                # ele obrigatoriamente passará pelo funil de 2^32 ao longo das divisões consecutivas!
                if expoente >= 4:
                    passou_pela_potencia = True
                    break
            if copia == 1:
                break

            # Regras tradicionais de Collatz
            if copia % 2 == 0:
                copia //= 2
            else:
                copia = 3 * copia + 1

        # Se passar em todas as condições, imprime o resultado IMEDIATAMENTE
        if passou_pela_potencia:
            encontrados += 1
            print(f"🎯 [{encontrados}] Número Encontrado: {triangular}")
            print(f"   --> Gerador Triangular (n): {n}")
            print(f"   --> Termina no dígito ímpar: {triangular % 10}")
            print(f"   --> Entrou no fluxo de potências em: 2^{expoente}")
            print("-" * 60)

            # Se quiser interromper no primeiro achado, descomente a linha abaixo:
            # break

    if encontrados == 0:
        print("Busca finalizada. Tente expandir o range de 'n' se necessário.")


if __name__ == "__main__":
    collatz_conjecture_an_idea()

