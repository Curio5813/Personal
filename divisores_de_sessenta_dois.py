def divisores_de_sessenta_dois():
    """
    Verifications about the number 62 and it's implications
    as the biggest gap between twin prime numbers and the next
    prime number not twin prime.
    :return:
    """
    primos, n, cont, modular, gaps, diffs = [], 62, 1, [], [], []
    for i in range(2, 50000 + 1):
        for j in range(2, 50000 + 1):
            if i % j == 0 and i == j:
                primos.append(i)
            if i % j == 0 and i != j:
                break
    print(*primos)
    for i in range(0, len(primos)):
        if i >= len(primos) - 1:
            break
        gaps.append(primos[i + 1] - primos[i])
    print(*gaps)
    print(primos[gaps.index(max(gaps))])
    for i in range(0, len(primos)):
        if primos[i] >= n:
            mod = primos[i] % n
            if mod not in primos:
                modular.append(mod)
        else:
            mod = n % primos[i]
            if mod not in primos:
                modular.append(mod)
    for i in range(0, len(modular)):
        if i >= len(modular) - 1:
            break
        diff = modular[i + 1] - modular[i]
        diffs.append(abs(diff))
    print(max(diffs))
    print(*diffs)


divisores_de_sessenta_dois()
