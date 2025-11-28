def numeros_tristes():
    limite = int(input("Limite: "))
    pares = []
    for n in range(1, limite + 1):
        soma = 0
        divisores, num = [], n
        for d in range(n - 1, 0, -1):
            if n % d == 0:
                divisores.append(d)
                soma += d
        if soma > 1:
            primo, flag = True, True
            for i in range(2, int(soma ** 0.5) + 1):
                if soma % i == 0:
                    primo = False
                    break
            if primo:
                print(f"{num} é triste → soma={soma}.")
                if n % 2 == 0:
                    pares.append(n)
    print("===================================================================")
    print("Diferença entre um numero triste par e o próximo numero triste par:")
    print("===================================================================")
    diff = []
    for i in range(1, len(pares)):
        print(pares[i] - pares[i - 1])
        diff.append(pares[i] - pares[i - 1])
    print(len(pares))
    print(f"Maior diferença encontrada entre números tristes pares: {max(diff)}")


if __name__ == "__main__":
    numeros_tristes()
