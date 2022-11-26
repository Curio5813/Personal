def collatz_conjecture():
    """
    This function treat about de Collatz Conjecture.
    :return:
    """
    lc, cont = [], 0
    num = int(input("Digit a integer positive number: "))
    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = 3 * num + 1
        lc.append(int(num))
        cont += 1
    print(cont)
    print(*lc)
    lc.sort()
    print(*lc)


collatz_conjecture()
