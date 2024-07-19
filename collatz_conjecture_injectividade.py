def collatz_conjecture_injectividade():
    """
    Collatz Conjecture é a injective function until its reach the value 2.
    :return:
    """
    num = int(input("Digit a integer positive number: "))
    par, pares, flag = [], [], 0
    while num != 2:
        if num % 2 == 0:
            par.append(num)
            num //= 2
            par.append(num)
            pares.append(par)
            par = []
        if num % 2 == 1:
            par.append(num)
            num = 3 * num + 1
            par.append(num)
            pares.append(par)
            par = []
    print(pares)
    for i in range(0, len(pares)):
        if pares.count(pares[i]) > 1:
            print(pares[i])
            print("The Collatz Conjecture is not a Injective Function!")
            flag = 1
    if flag == 0:
        print("The Collatz Conjecture is a Injective Function!")


collatz_conjecture_injectividade()
