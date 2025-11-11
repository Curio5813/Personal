def numeros_tristes():
    limite = 10000
    for n in range(1, limite + 1):
        soma = 0
        divisores, num = [], n
        for d in range(n - 1, 0, -1):
            if n % d == 0:
                divisores.append(d)
                soma += d
        if soma > 1:
            primo = True
            for i in range(2, int(soma ** 0.5) + 1):
                if soma % i == 0:
                    primo = False
                    break
            if primo:
                print(f"{num} é triste → soma={soma}")


numeros_tristes()
