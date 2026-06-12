def soma_dos_termos_de_uma_pa():
    """
    Calcula a Soma dos Termos de uma PA de razão q.
    :return:
    """
    q = int(input("Digite a razão da PA: "))
    n = int(input("Digite a quantidade de termos: "))
    a1, an = q, 1
    for i in range(n, 0, -1): # Achar o último termo.
        if i % q == 0:
            an = i
            break
    n = an / q # Acha o numero de termos
    soma = n * (an + a1) /2 # soma dos termos de razão q.
    print(f"O primeiro termo é: {a1}")
    print(f"O ultimo termo é: {an}")
    print(f"O numero de termos é: {int(n)}")
    print(f"A soma dos termos é: {int(soma)}")


soma_dos_termos_de_uma_pa()
