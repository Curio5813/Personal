def factoringNumbers():
    """
    This function decomposing numbers in prime products and its powers.
    :return:
    """
    num = int(input("Digit a integer positive numbers major than 1: "))
    cont1, cont2, l1, l2 = 2, 0, [], []
    while num > 1:
        while num % cont1 == 0:
            num //= cont1
            cont2 += 1
        else:
            if cont2 >= 1:
                l1.append(cont1)
                l2.append(cont2)
                cont1 += 1
                cont2 = 0
            else:
                cont1 += 1
    for i in range(0, len(l1)):
        if i == len(l1) - 1:
            return print(f"{l1[i]}^{l2[i]}")
        print(f"{l1[i]}^{l2[i]} * ", end="")


factoringNumbers()
print("")
print("It's All Folks")
