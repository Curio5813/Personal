def divisores_de_sessenta_dois():
    """
    Verifications about the number 62 and it's implications
    as the biggest gap between twin prime numbers.
    :return:
    """
    primos, n, cont, modular = [], 62, 1, []
    for i in range(2, 10000 + 1):
        for j in range(2, 10000 + 1):
            if i == 2:
                primos.append(i)
                break
            if i % j == 0 and i == j:
                primos.append(i)
            if i % j == 0 and i != j:
                break
    for i in range(0, len(primos)):
        if primos[i] > n:
            cont += 1
            n = 62 * cont
        else:
            mod = n % primos[i]
            if mod not in primos and mod not in modular:
                modular.append(mod)
    modular.sort()
    print(*modular)


divisores_de_sessenta_dois()
