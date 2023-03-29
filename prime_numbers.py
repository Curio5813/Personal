def generatePrimeNumbers():
    """
    This function give a list of prime numbers until a
    limit setted. This algorithm use the idea "The siege
    of Eratostenes".
    :return:
    """
    p, n_p, lim = [], set(), 1_000_000 + 1
    for i in range(2, lim):
        if i in n_p:
            continue
        for k in range(i * 2, lim, i):
            n_p.add(k)
        p.append(i)
    print(len(p))
    return print(*p)


generatePrimeNumbers()
