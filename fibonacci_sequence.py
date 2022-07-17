def fibonacciSequence():
    """
    This function return the fibonacci sequence until the term
    specified by the user.
    :return:
    """
    a, b, p, l = 0, 0, 1, []
    num = int(input("How many terms do you want have the fibonacci "
                    "sequence? "))
    for i in range(0, num):
        a, b, = b, p
        p = a + b
        l.append(a)
    return print(*l)


fibonacciSequence()
