def collatz_conjecture_injectividade():
    """
    Collatz Conjecture é a injective function until its reach the value 2.
    In the Collatz Conjecture, both the domain and the image of a function
    that observes such a construction in the plane are biunivocal, that is,
    for each even point there corresponds one and only one point in the
    function, therefore for each odd point, making the function binary or
    injective, which means that in the Collatz Conjecture, given any point
    without codomain we have only one point in the image, which, as in Projective
    Geometry, we end up calculating the inverse of the function, always
    leading to a power of 2, since the power of two will always be the inverse
    of the injection of the codomain into the image. Perhaps, assuming that
    domain and range are invertible in an injective function, it always tends
    to keep the relationship constant, just as we did, in numerical form in the
    Collatz Conjecture.
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
