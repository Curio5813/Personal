def primos_gemeos():
    """
    Acha todos o números primos gêmeos até 10.000 e sua distância para o próximo primo
    gêmeos ou não.
    :return:
    """
    n = int(input("Digite o limite: "))
    nao_primos, primos, gemeos, temp, distancias = set(), [], [], [], []
    for i in range(2, n + 1):
        if i in nao_primos:
            continue
        for j in range(i * 2, n + 1, i):
            nao_primos.add(j)
        else:
            primos.append(i)
    for i in range(len(primos)):
        for j in range(len(primos)):
            if i != j and primos[i] - primos[j] == 2:
                temp.append(primos[i])
                temp.append(primos[j])
                gemeos.append(temp)
                temp = []
    for i in range(len(gemeos)):
        for j in range(len(primos)):
            if gemeos[i][0] < primos[j]:
                distancias.append(primos[j] - gemeos[i][0])
                break
    print("Primo 1 - Primo 2 -> Distância ao próximo número primo:")
    for i in range(len(distancias)):
        print(f"{gemeos[i][1]:>5} -{gemeos[i][0]:>5} -> {distancias[i]}")
    maior_idx = distancias.index(max(distancias))
    print(*gemeos[maior_idx], end="")
    print(f": Maior Distância = {distancias[maior_idx]}")


if __name__ == '__main__':
    primos_gemeos()
