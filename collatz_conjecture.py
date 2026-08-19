import sys
from collections import deque

# Configuração obrigatória para o Python aceitar converter inteiros gigantescos
sys.set_int_max_str_digits(2_000_000)


def collatz_conjecture():
    """
    This function treats the Collatz Conjecture for a 2222-digit number.
    """
    # 1. Montagem do número com exatamente 2222 dígitos
    inicio = "2" * 32 + "3" * 3
    meio_e_fim = "1" * (1_413_721 - 35)
    numero_str = inicio + meio_e_fim

    n = int(numero_str)

    print(f"Comprimento do número validado: {len(numero_str)} dígitos (Múltiplo de 11!)")
    print("-" * 65)
    print("Iniciando o loop. Exibindo o progresso a cada 1.000 iterações:")
    print("-" * 65)

    cont = 0
    # Janela deslizante para armazenar apenas as últimas 10 iterações (guarda tuplas: (passo, valor))
    ultimas_iteracoes = deque(maxlen=30)

    # 3. Laço principal da Conjectura de Collatz
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1

        cont += 1

        # Guarda o estado atual na nossa janela deslizante
        ultimas_iteracoes.append((cont, n))

        # Print inteligente disparado rigorosamente a cada 1.000 iterações
        if cont % 1000 == 0:
            print(f"Iteração: {cont:<5} | Tamanho atual do número: {len(str(n))} dígitos")

    print("-" * 65)
    print("🎯 O número atingiu o loop final (1) com sucesso!")
    print(f"Total exato de iterações: {cont} passos.")
    print("-" * 65)

    # 4. Exibição das 10 últimas iterações salvas
    print("📋 DETALHE DAS 10 ÚLTIMAS ITERAÇÕES ANTES DO FIM:")
    for passo, valor in ultimas_iteracoes:
        print(f"Passo: {passo:<5} -> Valor atual: {valor}")

    return cont


if __name__ == "__main__":
    collatz_conjecture()
