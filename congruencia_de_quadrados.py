import math
from time import time

inicio = time()

def mdc(a, b):
    """Calcula o Máximo Divisor Comum de forma ultra rápida"""
    while b:
        a, b = b, a % b
    return a


def fatoracao_congruencia_quadrados(n):
    """
    Motor matemático focado em encontrar x^2 - y^2 = n.
    Altamente eficiente para chaves RSA onde p e q têm tamanhos próximos.
    """
    print(f"[*] A iniciar busca avançada para N = {n}")

    # 1. Começa na raiz quadrada inteira teto de N
    x = math.isqrt(n) + 1
    ciclos = 0

    while True:
        ciclos += 1
        # Calcula a diferença para verificar se mapeia um quadrado perfeito
        aux = x * x - n
        y = math.isqrt(aux)

        # Se for um quadrado perfeito, encontrámos a quebra da chave!
        if y * y == aux:
            p = x + y
            q = x - y
            print(f"[+] Sucesso! Encontrado em {ciclos} iterações.")
            return p, q

        x += 1

        # Salvaguarda para evitar loops infinitos em números inválidos
        if x > (n + 1) // 2:
            break

    return None, None


# =====================================================================
# ÁREA DE TESTE COM INPUT
# =====================================================================
if __name__ == "__main__":
    print("=== PROVEN FACTORIZATION ENGINE (RSA) ===")

    # Teste com uma chave pública gerada anteriormente (20 dígitos)
    # Exemplo estável: 10500000099500000209
    chave_input = input("Insira a Chave Pública (Módulo N): ").strip()

    if chave_input.isdigit():
        n = int(chave_input)

        p, q = fatoracao_congruencia_quadrados(n)

        print("-" * 50)
        if p and q and p != 1 and q != 1:
            print("[🎉 SUCESSO] Chaves privadas extraídas!")
            print(f"🔑 Fator p: {p}")
            print(f"🔑 Fator q: {q}")
            print(f"🔍 Validação (p * q == N): {p * q == n}")
        else:
            print("[-] Não foi possível fatorar com este método.")
    else:
        print("[-] Erro: Introduza apenas números.")

fim = time()

print(fim - inicio)
